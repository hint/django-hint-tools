#!/usr/bin/env python

"""
Build
"""

import glob
import os
import shutil

import djtools

# would be good not to overwrite old _djtools_common.py

for file in glob(djtools.get_skel_dir() + '/*'):
    shutil.copy(file, os.getcwd())