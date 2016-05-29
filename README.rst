Easy Web App (for Python)
=========================
Create web applications easily. 

This is a `PyPI package <https://pypi.python.org/pypi/easy-web-app>`_
for the `rest-web-gui <https://github.com/ma-ha/rest-web-ui>`_ framework.

Focus is on *web applications* (not simple web pages). 
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
   ``pip install easy-web-app``
   
Create first web app with Python:
---------------------------------
Create a file, e.g. ``firstapp.py``  
  
::

	from easywebapp.webapp import Portal 
	import easywebapp.page_layout as page
	
	mainpage = page.PageLayout( 'First Page' )
	
	# initialize portal
	portal = Portal( 'My Portal', 8000, mainpage )
	
	# create a single view
	view1 = page.View( 'View1', 'Example View', 'none' )
	mainpage.getRows().addView( view1, '300px' )
	
	
	# define a custom web service 
	portal.addURL( '/myservice', 'myservice' )
	
	class myservice:
	    def GET( self ):
	        return 'Hello World'
	
	# start the web server
	portal.run()

TODOs
-----
- [x] First working *rest-web-ui* integration
- [x] PyPI package
- [ ] configure port from init
- [ ] business services API
- [x] portal.getPage( name )  
- [x] portal.addPage( pageId [, title] [, viewDef] [, viewConfig] ) 
- [ ] Portal pages navigation tabs
- [x] page.addView( def [, config]  )
- [x] page.addColumnsRow( id, width )
- [x] row.addView( def [, config] )
- [x] row.addColumnsRow ( id, height )
- [x] column.addView ( def [, config] )
- [x] column.addRowsColumn ( id, width )  
- [x] View API
- [ ] I/O server and API
