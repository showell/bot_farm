import os
import subprocess
import sys

def get_root_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

SUPERVISORD_HELP = '''
SUCCESS!

You just started the supervisord program,
which in turn started our bot processes.

You can use this command to check out on their status:

    supervisorctl status

You can also use the web interface: http://localhost:9001/

You can start/stop individual bots using either the web interface
or supervisorctl.  Use this command to get help:

    supervisorctl help

You can shut down everything, including supervisord itself, as follows:

    supervisorctl shutdown
'''

WORKER_TEMPLATE = '''
[program:bot-farm-%(name)s]
command=python %(run_py)s %(lib_path)s --config-file %(zuliprc_path)s
'''

def join(dir, fn):
    return os.path.abspath(os.path.join(dir, fn))

def get_worker_config(bots, root_path):
    '''
    Return the supervisord configuration for our bot workers.
    '''
    text = '; CODE-GENERATED CONFIG FOLLOWS\n'
    for bot in bots:
        run_py = join(root_path, 'zulip/contrib_bots/run.py')
        lib_path = join(root_path, bot['lib'])
        zuliprc_path = join(root_path, bot['zuliprc'])
        text += WORKER_TEMPLATE % dict(
            run_py=run_py,
            name=bot['name'],
            lib_path=lib_path,
            zuliprc_path=zuliprc_path)

    return  text

def run():
    root_path = get_root_path()

    sys.path.append('../../config')
    from bot_config import BOTS
    worker_config = get_worker_config(bots=BOTS, root_path=root_path)

    template_fn = 'supervisord.conf.template'
    template_payload = open(template_fn).read()
    conf_fn = 'supervisord.conf'
    conf_payload = template_payload % dict(worker_config=worker_config)
    open(conf_fn, 'w').write(conf_payload)
    try:
        result = subprocess.call([
            'supervisord',
            '-c', conf_fn
            ])
    except OSError:
        print('''
            It appears you need to install supervisord
            first.
            ''')
        sys.exit(1)

    if result == 2:
        print('''
            You probably had your old bots running.
            Try:
                supervisorctl shutdown
            ''')
        sys.exit(1)
    elif result != 0:
        sys.exit(1)

    print SUPERVISORD_HELP

if __name__ == '__main__':
    run()
