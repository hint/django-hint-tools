import os

def rsync(basedir, src, dest):
    #rsync --checksum --compress --exclude '.svn' --links --perms --progress --recursive --update --verbose $BASEDIR$1 $2
    print basedir, src, dest
    return 