tools_update_requirements
=========================

Usage:

    manage.py tools_update_requirements

Make new `requirements-*.txt` file aka freeze your virtualenv.

This will generate a requirements.txt for your current Python version. 2.5.1
and 2.5.2 will share one file, while 2.5 and 2.6 wont.

This script should be run every time you install new Python modules using pip
inside your virtualenv.
