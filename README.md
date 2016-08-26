# bot_farm
This project will have various examples of deploying bot code for Zulip.

## Borrowed Code

Note that this project contains files in the "zulip" directory that
are copied from https://github.com/zulip/zulip under the terms of its
license (Apache).

The rest of this project is under the MIT license.

## Overview

The goal for this project is to serve as a template for folks who need
help deploying Zulip bots in their own customized setups.  It is
meant to be reusable, but mostly likely reuse scenarios would involve
forking this project, as a lot of the project is about configuration.

## Structure

This project has three main pieces, all of which correspond to a top
level directory.

### zulip

The zulip directory contains example libraries for simple Zulip
custom apps.  These essentially get turned into either bots or
webhooks by generic drivers.

### config

The config directory will contain configuration for deploying your
bots, and it is also the directory into which you will want to
(carefully) drop your zuliprc configurations for the Zulip users
you are going to connect to your apps.

### deployments

There are different ways to deploy custom apps on Zulip, and the
deployments directory will include different deployment strategies

Each subdirectory beneath deployments will have a startup.py script
that will launch processes that implement the bots.  This is still a
work in progress, but essentially, the two main ways to deploy custom
apps is either as long-running bots or as webhooks, and then within
those types there may be different variations, depending, for example,
on how you like to do your web hosting.



