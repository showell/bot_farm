import subprocess
import sys

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

def run():
    template_fn = 'supervisord.conf.template'
    template_payload = open(template_fn).read()
    conf_fn = 'supervisord.conf'
    conf_payload = template_payload
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
