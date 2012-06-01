import os

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    args = '<[filename]>'
    help = 'Create buildenv.sh script'

    template = """#!/usr/bin/env bash

new_virtualenv() {
    if [ -d "_oldenv" ]; then
        rm _oldenv -rf
    fi
    if [ -d "_env" ]; then
        mv _env _oldenv
    fi
    virtualenv _env --distribute

    # there were permission issues in shared environment under Gentoo
    # but the following line can potentially remove temporary files
    # needed by other programs
    # find /tmp/* -user `whoami` -exec rm -rf {} \; >& /dev/null
}

OLDDIR=`pwd`
SELF=`dirname $0`
PYVERSION=`python -V 2>&1 | sed 's Python\ \([0-9\.]*\) \\1 ' | cut -c -3`

cd $SELF

if [ "$1" == "--full" ]; then
    new_virtualenv
fi

if [ ! -d "_env" ]; then
    new_virtualenv
fi

. _env/bin/activate
pip install -r pip-requirements-$PYVERSION.txt
deactivate

cd $OLDDIR
    """

    def handle(self, *args, **options):
        try:
            filename = args[0]
        except IndexError:
            filename = 'buildenv.sh'

        # skip absolute paths
        if not filename.startswith('/'):
            fullname = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', filename)

        try:
            open(fullname, 'r')
            raise CommandError('File already exists, exiting...')
        except IOError:
            pass

        f = open(fullname, 'w')
        f.write(self.template)
        f.close()
        os.chmod(fullname, 0755)

        self.stdout.write("Successfully written buildenv script to %s\n" % os.path.abspath(fullname))