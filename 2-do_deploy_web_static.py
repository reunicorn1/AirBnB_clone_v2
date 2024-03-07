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
    print(filename)
    run("tar -xzvf {} - C /data/web_static/releases/".format(filename))
    run("rm /tmp/{}".format(archive_path.split('/')[-1]))
    run("ln -s --force /data/web_static/releases/{} /data/web_static/current".format(filename))
    return True
