#!/usr/bin/python3
"""This fabric script generates a .tgz archive from the contents of the
web_static folder."""

from fabric.api import *
from datetime import datetime
import os
env.hosts = ['54.90.8.245', '18.204.16.25']
env.user = 'ubuntu'


def do_pack():
    """Generates a .tgz archive."""
    try:
        local('mkdir -p versions')
        dt = datetime.now()
        date_string = "{0:%Y}{0:%m}{0:%d}{0:%H}{0:%M}{0:%S}".format(dt)
        archive_name = 'versions/web_static_{}.tgz'.format(date_string)

        local("tar -czvf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None


def do_deploy(archive_path):
    """deploys to server"""

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
    except Exception:
        return False


def deploy():
    """Creates and deploys archive"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)


def do_clean(number=0):
    """Deletes out-of-date archives

    Args:
        number (int, optional): number of archives to keep. Defaults to 0.
    """
    if number == 0:
        number = 1

    local("cd versions ; ls -t | sed '1,{}d' | xargs rm -rf".format(number))
    path = "/data/web_static/releases"
    run("cd {} ; ls -t | sed '1,{}d' | xargs rm -rf".format(path, number))
