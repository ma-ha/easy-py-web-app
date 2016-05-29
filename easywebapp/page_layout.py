# Copyright (c) 2016 ma-ha, The MIT License (MIT)
import json

from custom_json import ObjectEncoder

class Footer:
    def __init__( self ):
        self.copyrightText = "Powered by <a href=\"https://github.com/ma-ha/rest-web-ui\">'Portal NG' {{PONGVER}}</a>, &copy; 2016, MH."
        self.linkList = [ { "text":"About", "url": "index.html?layout=about"} ]
        self.modules = [ { "id": "feedbackView", "type": "pong-feedback", "param": { } } ]       

class Rows:
    rows = None
    def __init__( self ):
        self.rows =  []

    def to_json(self):
        return self.rows
    
    def addView(self, view, height ):
        view.setRowId( view.id )
        view.setHeight( height )  
        self.rows.append( view )
    
class View:
    def __init__( self, id, title, resourceURL ):
        self.id = id
        self.title = title
        self.resourceURL = resourceURL
        self.decor = 'decor'
        
    def setRowId(self, id ):
        self.rowId = id 
        
    def setHeight(self, height ):
        self.height = height
        
    def setWidth(self, width ):
        self.width = width
        
class Page:
    rows = None
    def __init__( self, title ):
        self.title  = title
        self.header = { 'logoText':title, 'modules':[] }
        self.rows   = Rows()
        self.rows.addView( View( 'View1', 'View 1', 'none' ), '400px' )
        #self.rows.addView( View( 'View2', 'View 2', 'none' ), '300px' )
        self.footer = Footer()
    
    def getRows(self):
        return self.rows
    
class PageLayout:
    portal = None
    page = {}
    def __init__( self, title ):
        self.page = Page( title )

    def addToPortal( self, portal ):
        self.portal = portal

    def getRows(self):
        return self.page.getRows()
        

    def to_JSON(self):
        if self.portal != None :
            self.page.title  = self.portal.getTitle() 
            self.page.header = self.portal.getHeader()
        print json.dumps( self.page, cls=ObjectEncoder, indent=2, sort_keys=False)
        return json.dumps( self.page, cls=ObjectEncoder, indent=2, sort_keys=False)
        #return json.dump( self.page, cls=ObjectEncoder, indent=2, sort_keys=True)
        #return json.dumps( self.page, default=lambda o: o.__dict__ )
