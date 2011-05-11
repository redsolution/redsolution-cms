======================
Redsolution CMS README
======================

Development Lyrics:
===================

We've been developing Django sites 4 years. We made many sites and came to the 
conclusion:

- Standard function should be performed with standard libraries.
- Those libraries should be maintained separately from the production site.
- Libraries should be easily supported

After all, we decided to create a product which would help us to bulid site with 
latest stable versions of standard modules. `zc.buildout`_ was appropriate tool,
but most of modules needs to be configured, configurations differs from one 
module version to another. Buildout can't handle configuration options like 
`django.conf.settings` or urls. 
Also we want to escape from design process and bugfixes. Webdesign should be
created with web designers.
We decided that our product should be able to make a website template, ready for
further development and customizing.

.. _zc.buildout: http://www.buildout.org/

Features:
=========

- Web wizard site creation
- Portable crossplatform code
- Work with Python Package Index

Installation:
=============

From setup package
------------------

Download package for your system from `our site`_  and install it.

Create new folder, in which you you want to install site. In console, from that folder
run ::

    redsolutioncms  

Thats's all. CMS will download Django and some nessesary libraries and open web 
browser window (or tab) with first step of wizard. At the end of wizard you will
get website installed in specified folder, also installable on production server.

.. _our site: http://www.redsolutioncms.org/pages/download

From source
-----------

Download source distribution, or clone repository from `github`_. Just like when
you install from package, create a folder. Extend your system environment variable
``PYTHONPATH``: ::

    $ export PYTHONPATH=<path-to-redsoultioncms-folder>

(on windows use ``set PYTHONPATH=<path-to-redsoultioncms-folder>``)

and run loader: ::

    $ <path-to-redsoultioncms-folder>/redsolutioncms/loader.py

Then you will et the same results.

.. _github: http://github.com/redsolution/redsolution-cms


For more documentation, visit: http://www.redsolutioncms.org