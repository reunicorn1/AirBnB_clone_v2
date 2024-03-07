#!/usr/bin/python3
"""
1. Compress before sending
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    This function archieves contents of the web_static folder
    """
    c = datetime.now()
    filename = "versions/web_static_{}.tgz".format(c.strftime("%Y%m%d%H%M%S"))
    value = local('mkdir -p versions && tar -czvf {} web_static'
                  .format(filename))
    if value.failed:
        return None
    return filename
