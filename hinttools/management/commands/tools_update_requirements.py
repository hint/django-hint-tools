import os
import sys

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    args = ''
    help = 'Update project requirements'

    def handle(self, *args, **options):
        pyversion = '%s.%s' % (sys.version_info[0], sys.version_info[1])
        filepath = os.path.join(os.path.dirname(sys.argv[0]), '..',
                                'pip-requirements-%s.txt' % pyversion)

        sys.stdout = open(filepath, 'w')
        os.system('pip freeze -r %s > %s' % (filepath, filepath))
