#!/usr/bin/python3
''' make a tgz archive '''
from fabric.api import local, sudo
from datetime import datetime


def do_pack():
    try:
        local('mkdir versions; tar -cvzf versions/web_static_{}.tgz\
        web_static'.format(datetime.now().strftime('%Y%m%d%H%M%S')))
    except Exception:
        return None
