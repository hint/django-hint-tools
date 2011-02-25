django-centralniak-tools
========================

Installation
------------
You should use ./build.sh to download latest version of tools from github, and 
COPY them to your desired directory. Existing files will be erased, directories
will be merged. If reading for the first time, read the preceding sentence once
more. Thank you! :)

Tools
-----

Right now, it's Just a listing of what I'd like to have bundled in this repo...

1. buildenv.sh -> virtualenvbuild (MultiPL)
2. copy_mysqldb.sh -> mysqlcopylocal (MultiPL)
3. make_crontab.py -> crontabbuild (MultiPL)
4. runserver.py + restartserver.py -> djangoserver (MultiPL, large changes)
5. update_requirements.sh -> requirementsbuild (MultiPL?)
6. indexsphinx.sh -> sphinxindex (MAM)
7. media_sync.sh -> to be written -- should use rsync to sync media with 
   another django instance 
8. runsphinx.sh -> sphinx (MAM)
9. runtest_*.sh -> test (MAM)
10. stopsphinx.sh -> sphinxstop (MAM)
11. commit_and_dump.sh -> mysqldump (MultiPL, large changes)
12. set_collation_many.py -> mysqlcollationmany (MultiPL)
13. pack_locales.sh -> localepack (Baltic)
14. WSGI? 

Each of the scripts, should have as much hooks as possible.

There must be a buildscript to quickly synchronise with your project directory.