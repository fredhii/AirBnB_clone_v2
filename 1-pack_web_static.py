#!/usr/bin/python3
''' make a tgz archive '''
from fabric.api import *
from datetime import datetime
import os


def make_dir(routing, name_pack):
    with hide('running'):
        local('mkdir -p versions')
    local('tar -cvzf {} {}'.format(routing, name_pack))
    with hide('running'):
        size = local('stat -c %s ./{}'.format(routing), capture=True)
    return size


def do_pack():
    try:
        name_pack = 'web_static'
        routing = 'versions/web_static_{}.tgz'.\
                  format(datetime.now().strftime('%Y%m%d%H%M%S'))
        init = 'Packing {} to {}'.format(name_pack, routing)
        print(init)
        size = make_dir(routing, name_pack)
        print('{} packed: {} -> {}'.format(name_pack, routing, size))
        return '{}/{}'.format(os.getenv('PWD'), routing)
    except Exception:
        return None
