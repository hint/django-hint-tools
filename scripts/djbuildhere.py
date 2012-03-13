#!/usr/bin/env python

"""
Build
"""

import glob
import os
import shutil
import sys

try:
    import djtools
# this is for testing purposes
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    import djtools

# would be good not to overwrite old _djtools_common.py

if len(sys.argv) > 1:
    destdir = sys.argv[1]
else:
    destdir = os.getcwd()

for file in glob.glob(djtools.get_skel_dir() + '/*'):
    shutil.copy(file, destdir)