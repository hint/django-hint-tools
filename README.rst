========================
django-centralniak-tools
========================

django-centralniak-tools aims at easing some common django tasks over console.

Features:

- yet
- to
- be
- written

Contributions and comments are welcome using Github at: 
http://github.com/centralniak/django-centralniak-tools

Please note that in order to take full advantage of  django-centralniak-tools
you need:

- rsync

Installation
============

#. `pip install django-centralniak-tools`
#. Run `djbuildhere` optionally passing directory path where the entry scripts
   will be built. If you don't pass the path, the entry scripts will be copied
   to current directory.

If you need to upgrade you tools installation, run
`pip install django-centralniak-tools --upgrade` and rerun `djbuildhere`.
Your configuration won't be overwritten!

Configuration
=============

See _djtools_common.py in the directory, where buildscripts were installed.
The varialble names should be fairly self-explanatory.

Usage
=====

rsync
-----

Uses rsync to incrementally download media from production servers. Just
configure the source, destination and media directories for your django
installation. The default rsync command should be fine, but you can adjust it
in case you want to limit the bandwidth etc.

Bugs & Contribution
===================

Please use Github to report bugs, feature requests and submit your code:
http://github.com/centralniak/django-centralniak-tools

:author: Piotr Kilczuk
:date: 2012/03/13