#!/usr/bin/python3
""" Fabric script to create tarball"""
import tarfile
import os
from datetime import datetime
from fabric.api import *


def do_pack():
    """ the function """
    t = datetime.now()
    filename = f"web_static_{datetime.now().strftime('%Y%m%d%H%M%S')}.tgz"
    if not os.path.exists('versions'):
        os.mkdir('versions')
    with tarfile.open(f"versions/{filename}", "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists(f"versions/{filename}"):
        return f"versions/{filename}"
    else:
        return None


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


def deploy():
    """ function to deploy archive """
    file_name = do_pack()
    if not file_name:
        return False
    else:
        return do_deploy(file_name)
