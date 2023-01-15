#!/usr/bin/python3
"""This fabric script generates a .tgz archive from the contents of the
web_static folder."""

from fabric.api import *
from datetime import datetime


def do_pack():
    """Generates a .tgz archive."""
    try:
        local('mkdir -p versions')
        dt = datetime.now()
        date_string = "{0:%Y}{0:%m}{0:%d}{0:%H}{0:%M}{0:%S}".format(dt)
        archive_name = 'web_static_{}'.format(date_string)

        local("tar -czvaf versions/{}.tgz web_static".format(archive_name))
        return archive_name
    except Exception:
        return None
