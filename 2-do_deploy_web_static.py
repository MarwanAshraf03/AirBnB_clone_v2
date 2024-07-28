#!/usr/bin/python3
""" Fabric script to create tarball"""
import tarfile
import os
from datetime import datetime
from fabric.api import *


env.hosts = ['54.197.49.59', '18.206.197.251']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ the function """
    if not os.path.exists(archive_path):
        return False
    single_name = archive_path.split('/')[1]
    put(archive_path, '/tmp/')
    run(f"mkdir -p /data/web_static/releases/{single_name[:-4]}/")
    run(f'tar -xzf /tmp/{single_name} -C /data/web_static/relea'
        f'ses/{single_name[:-4]}/')
    run(f'rm /tmp/{single_name}')
    run(f'mv /data/web_static/releases/{single_name[:-4]}/web_static/* '
        f'/data/web_static/releases/{single_name[:-4]}/')
    run(f'rm -rf /data/web_static/releases/{single_name[:-4]}/web_static')
    run('rm -rf /data/web_static/current')
    run(f'ln -s /data/web_static/releases/{single_name[:-4]}/ '
        f'/data/web_static/current')
    return True
