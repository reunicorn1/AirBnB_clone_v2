#!/usr/bin/python3
"""
1. Compress before sending
"""
from fabric.api import run


def do_pack():
    """
    This function archieves contents of the web_static folder
    """
    run('tar -czvf versions/web_static_$(date +%Y%m%d%H%M%S).tgz web_static')
    value = run('find . -name web_static_*.tgz')
    return(value.stdout.strip())
