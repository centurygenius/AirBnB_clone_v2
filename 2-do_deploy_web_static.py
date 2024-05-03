#!/usr/bin/python3
# Fabric script that distributes an archive
# to my web servers web-01 and web-02
# using the do_deploy function
import os
from fabric.api import run, put, env

env.hosts = ['54.164.91.175', '100.26.171.162']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Create a tar gzipped archive of the directory web_static."""
    if os.path.exists(archive_path) is False:
        return False
    else:
        try:
            put(archive_path, "/tmp/")
            file_name = archive_path.split("/")[1]
            file_name2 = file_name.split(".")[0]
            final_name = "/data/web_static/releases/" + file_name2 + "/"
            run("mkdir -p " + final_name)
            run("tar -xzf /tmp/" + file_name + " -C " + final_name)
            run("rm /tmp/" + file_name)
            run("mv " + final_name + "web_static/* " + final_name)
            run("rm -rf " + final_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + final_name + " /data/web_static/current")
            print("New version deployed!")
            return True
        except Exception as e:
            print(e)
            return False

