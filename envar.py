import os
import sys
import platform

def find_os():
    osys = platform.system()
    osys_ver = platform.release()
    if osys == 'Darwin' and osys_ver < '19.0.0':
        rc = '.bashrc'


def set_envar():
    platform = sys.platform
