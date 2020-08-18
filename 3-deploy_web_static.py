#!/usr/bin/python3
''' make a tgz archive '''
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['34.74.22.156', '34.74.179.134']


def make_dir(routing, name_pack):
    ''' create directory and package '''
    with hide('running'):
        local('mkdir -p versions')
    local('tar -cvzf {} {}'.format(routing, name_pack))
    with hide('running'):
        size = local('stat -c %s ./{}'.format(routing), capture=True)
    return size


def do_pack():
    ''' print every message '''
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


def do_deploy(archive_path):
    ''' deploy '''
    if os.path.isfile(archive_path):
        name = archive_path.split('/')[-1]
        put(archive_path, '/tmp/{}'.format(name))
        run('mkdir -p /data/web_static/releases/{}/'.format(name))
        run('tar -xzf /tmp/{0} -C /data/web_static/releases/{0}/'.format(name))
        run('rm /tmp/{}'.format(name))
        run('mv /data/web_static/releases/{0}/web_static/*\
        /data/web_static/releases/{0}/'.format(name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
            format(name))
        print('New version deployed!')
        return True
    else:
        return False


def deploy():
    path = do_pack()
    if path is None:
        return False
    return (do_deploy(path))
