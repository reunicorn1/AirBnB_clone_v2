#!/usr/bin/python3
"""
2. Deploy archive!
"""
from fabric.api import run, put, env, cd
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
        result1 = run("mkdir -p /data/web_static/releases/{}".format(filename))
        result2 = run("tar -xzvf {}.tgz -C /data/web_static/releases/{}"
                      .format(filename, filename))
        if result1.failed or result2.failed:
            return False
    result1 = run('cp -R /data/web_static/releases/{}/web_static/* '
                  '/data/web_static/releases/{}/ && rm -rf /data/web_static/'
                  'releases/{}/web_static'
                  .format(filename, filename, filename))
    result2 = run("rm /tmp/{}.tgz".format(filename))
    result3 = run("rm /data/web_static/current")
    result4 = run("ln -s /data/web_static/releases/{} /data/web_static/current"
                  .format(filename))
    if result1.failed or result2.failed or result3.failed or result4.failed:
        return False
    return True
