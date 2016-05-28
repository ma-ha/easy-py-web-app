# Copyright (c) 2016 ma-ha, The MIT License (MIT)
import web
import os

templatesdir = os.path.join( os.path.dirname( __file__  ), 'templates/' )

#print templatesdir
render = web.template.render( templatesdir )

portal_pages = {}  

class Portal:
    # dictionary of pages
    # urls for web.py
    urls = (
        '/', 'index',
        '^/svc/layout/(.*)', 'layout'
    )
    title = 'My New Portal'

    def __init__( self, port, main_page ):
        portal_pages['main/structure'] = main_page 
        main_page.addToPortal( self )
        self.app = web.application( self.urls, globals() )
        
    def getApp(self):
        return self.app
    
    def addPage( self, page_name, page ):
        portal_pages[ page_name, page ]

    def getPage( self, page_name ):
        return portal_pages[ page_name ]
    
    def addURL(self, url_pattern, url_class ):
        self.urls = self.urls + ( url_pattern, url_class )    
        
    def run(self):    
        print 'Start server...' 
        self.app.run()
        
    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title
    
    def getHeader(self):
        header = {}
        header['logoText'] = self.title
        modules = [] 
        return header


class index:
    def GET( self ):
        return render.index()
 
class layout:
    def GET( self, x ):
        print 'in structure: '+x
        web.header('Content-Type', 'application/json')
        layout = portal_pages[x]
        return '{"layout":'+ layout.to_JSON() +'}' 
