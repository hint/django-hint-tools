#!/usr/bin/env python

"""
Build
"""

import os
import shutil

import djtools

# would be good not to overwrite old _djtools_common.py

shutil.copy(djtools.get_skel_dir(), os.getcwd())