tools_make_buildenv_script
==========================

Usage:

    manage.py tools_make_buildenv_script [script_name_incl_path]

Make buildenv.sh shell script that builds a virtualenv basing on your requirements file. This is a regular shell file,
that won't use Django in any way, because at the point it's likely that you don't have a virtualenv yet.

``script_name_incl_path`` is an absolute path to where a file shall be created. If empty, the file is created in the
directory superior to where your manage.py is located.

The requirements file will be named ``pip-requirements-[python.version].txt``. This can seem redundant at a first
glance, but some requirements will throw errors when requirements file was built on other Python version that the
buildenv.sh is being run on (for example external requirement importlib was moved to core in Python 2.7).