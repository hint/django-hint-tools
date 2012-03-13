import os

def get_skel_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'skel'))

def rsync(basedir, src, dest):
    #rsync --checksum --compress --exclude '.svn' --links --perms --progress --recursive --update --verbose $BASEDIR$1 $2
    print basedir, src, dest
    return 