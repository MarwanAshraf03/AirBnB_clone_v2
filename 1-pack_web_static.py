#!/usr/bin/python3
""" Fabric script to create tarball"""
import tarfile
import os
from datetime import datetime


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
