#!/usr/bin/env python

"""
Build
"""

import os
import shutil

PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

# would be good not to overwrite old _djtools_common.py

shutil.copy(os.path.join(PACKAGE_ROOT, 'data', 'skel', '*'), os.getcwd())