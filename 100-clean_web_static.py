#!/usr/bin/python3
"""
4. Keep it clean!
"""
from fabric.api import run. local, cd, lcd

env.hosts = ['100.27.11.128', '54.209.192.180']


def do_clean(number=0):
    """
    This function deletes out-of-date archives
    """
    if number == 0:
        number = 1
    with lcd('/versions'):
        results = local("ls web_static* | head -n -{}".format(number)).split('\n')
        for result in results:
            local("rm -rf {}".format(result))
    with cd('/data/web_static/releases'):
        results = run("ls web_static* -d | head -n -{}".format(number)).split('\n')
        for result in results:
            run("rm -rf {}".format(result))


