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
    with lcd('versions'):
        local_archives = sorted(os.listdir('.'))
        archives_to_delete = local_archives[:-number]
        for archive in archives_to_delete:
            local('rm -f {}'.format(archive))

    with cd('/data/web_static/releases'):
        remote_archives = run('ls -tr').split()
        archives_to_delete = remote_archives[:-number]
        for archive in archives_to_delete:
            run('rm -f {}'.format(archive))
