#!/usr/bin/python3
"""This fabric script distributes an archive to web servers."""

from fabric.api import *
import os


env.hosts = ['54.90.8.245', '18.204.16.25']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """deploys to servers"""
    try:
        if os.path.isfile(archive_path) is False:
            return False
        archive_name = archive_path.split('/')[-1]
        file_name = archive_name.split('.')[0]
        path = "/data/web_static/releases/{}".format(file_name)
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(path))
        run('tar -xvf /tmp/{} -C {}'.format(archive_name, path))
        run('rm -r /tmp/{}'.format(archive_name))
        run('mv {0}/web_static/* {0}/'.format(path))
        run('rm -r /data/web_static/current')
        run('ln -sf {}/ /data/web_static/current'.format(path))
        return True
    except Exception:
        return False
