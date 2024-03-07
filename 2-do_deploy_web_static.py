#!/usr/bin/python3
"""
2. Deploy archive!
"""
from fabric.api import run, put
import os

env.hosts = ['100.27.11.128', '54.209.192.180']
def do_deploy(archive_path):
    """
    This function distributes an archive in your web server
    """
    if not os.path.exists(archive_path):
        return False
    put(archive_path, "/tmp")
    filename = archive_path.split('/')[-1].split('.')[0]
    with cd("/tmp"):
        run("mkdir -p /data/web_static/releases/{} && tar -xzvf {}.tgz - C /data/web_static/releases/{}".format(filename, filename, filename))
    run("rm /tmp/{}.tgz".format(filename))
    run("ln -s --force /data/web_static/releases/{} /data/web_static/current".format(filename))
    return True
