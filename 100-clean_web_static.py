#!/usr/bin/python3
"""
4. Keep it clean!
"""
from fabric.api import run, local, cd, lcd, env

env.hosts = ['100.27.11.128', '54.209.192.180']


def do_clean(number=0):
    """
    This function deletes out-of-date archives
    """
    number = 1 if int(number) == 0 else int(number)
    with lcd('./versions'):
        results = local("ls web_static* | sort", capture=True)
        results = sorted(results.stdout.split('\n'))[:-number]
        for result in results:
            local("rm {}".format(result))
    with cd('/data/web_static/releases'):
        results = run("ls -tr web_static_* -d").split()
        results = results[:-number]
        for result in results:
            run("rm -rf {}".format(result))
        if run.failed:
            print(yes)
