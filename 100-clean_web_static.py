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
    with lcd('./versions'):
        results = local("ls web_static* | sort", capture=True)
        results = sorted(results.stdout.split('\n'))[:-int(number)]
        for result in results:
            local("rm -rf {}".format(result))
