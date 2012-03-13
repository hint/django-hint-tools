#!/usr/bin/env python

# do not use this file

import glob
import os
import stat

add = glob.glob('src/djtools/data/skel/*') + glob.glob('scripts/*')
revoke = ['src/djtools/data/skel/_djtools_common.py']

for path in add:
    os.chmod(path, 00755)

for path in revoke:
    os.chmod(path, 00644)