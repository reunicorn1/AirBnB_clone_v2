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
    if number == 0:
        number = 1
    print(number)
    with lcd('./versions'):
        results = local("ls web_static* | sort", capture=True)
        results = sorted(results.stdout.split('\n'))[:-int(number)]
        for result in results:
            local("rm -rf {}".format(result))
    with cd('/data/web_static/releases'):
        results = run("ls web_static* -d | sort")
        results = sorted(results.stdout.split('\r\n'))[:-int(number)]
        for result in results:
            run("rm -rf {}".format(result))
