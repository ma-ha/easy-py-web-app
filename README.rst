Easy Web App (for Python)
=========================
Create web applications easily. 

This is a `PyPI package <https://todo>`_
for the `rest-web-gui <https://github.com/ma-ha/rest-web-ui>`_ framework.

Focus is on _web applications_ (not simple web pages). 
A lot of plug-ins are available to get a portal it quickly configured:

- Forms
- Tables / lists
- Content: via MediaWiki API, plain HTML views, or help dialogs
- I/O: control switches/drawer, gauges, graphs, LEDs, displays, ...
- i18n: switch language
- Maps: POIs, routes, traffic, ...
- Page to page navigation with navigation tabs, menus, links and session data
- Source code display
- Security: HTTP Basic authentication or OAuth 
- ...

This is how it may look like:

.. image:: https://raw.githubusercontent.com/ma-ha/easy-web-app/master/examples/demo-screen.png

Check out the `online demos <http://mh-svr.de/pong_dev>`_.

Remark: It is also available as `Node.js API package <https://www.npmjs.com/package/easy-web-app>`_.

Getting started
===============
Prepare:
--------
1. Create a web application project folder, e.g.
   ``mkdir ~/myapp``
2. Create a virtual Python environment for this folder:
   ``virtualenv ~/myapp``
3. Change into the project folder and activate the virtual environment:
   ``cd ~/myapp; source bin\activate``
4. Install this package:
   _TBD_

Create first web app with Python:
---------------------------------
Create a file, e.g. ``firstapp.py``  
  
.. code:: python

    # Copyright (c) 2016 ma-ha, The MIT License (MIT)
    import webapp
    # initialize portal
    portal = webapp.Portal( { 'title':'Test' } )
    # define a custom web service 
    portal.addURL( '/greet', 'greet' )
    class greet:
        def GET( self ):
            return 'Hello World!'
    # start the web server
    portal.run()

TODOs
-----
- [x] First working _rest-web-ui_ integration
- [ ] PyPI package
- [ ] portal.getPage( name )  
- [ ] portal.getPages()  
- [ ] page.addView( def [, config]  )
- [ ] page.addColumnsRow( id, width )
- [ ] row.addView( def [, config] )
- [ ] row.addColumnsRow ( id, height )
- [ ] column.addView ( def [, config] )
- [ ] column.addRowsColumn ( id, width )  
- [ ] portal.addPage( pageId [, title] [, viewDef] [, viewConfig] ) incl automatic navigation tabs
- [ ] I/O server and API
