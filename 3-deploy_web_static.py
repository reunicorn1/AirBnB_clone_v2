#!/usr/bin/python3
"""
3. Full deployment
"""

from fabric.api import local
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

env.hosts = ['100.27.11.128', '54.209.192.180']


def deploy():
    """
    This function created and distributes an archive to your webserver
    """
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
