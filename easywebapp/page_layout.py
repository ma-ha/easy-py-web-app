# Copyright (c) 2016 ma-ha, The MIT License (MIT)
import json

from custom_json import ObjectEncoder


class Rows:
    viewList = None
    columnId = None
    width    = None
    
    def __init__( self, columnId=None, width=None ):
        self.viewList =  []
        if columnId != None:
            self.columnId = columnId
            self.width    = width


    def to_json(self):
        if self.columnId == None:
            return self.viewList
        else:
            return { 'columnId':self.columnId, 'width':self.width, 'rows':self.viewList }
    
    def addView(self, view, height ):
        view.setRowId( view.id )
        view.setHeight( height )  
        self.viewList.append( view )
        
    def addColumnsRow( self, rowId, height ):
        col = Column( rowId, height )
        self.viewList.append( col )
        return col
    
class Column:
    rowId  = ''
    height = ''
    cols = None
    
    def __init__( self, rowId, height ):
        self.rowId  = rowId
        self.height = height
        self.cols   =  []

    #def to_json(self):
    #    return self.cols
    
    def addView(self, view, width ):
        view.setColumnId( view.id )
        view.setWidth( width )  
        self.cols.append( view )
        
    def addRowsColumn( self, columnId, width ):
        row = Rows( columnId, width )
        self.cols.append( row )
        return row
    
class View:
    def __init__( self, id, title, resourceURL ):
        self.id = id
        self.title = title
        self.resourceURL = resourceURL
        self.decor = 'decor'
        
    def setRowId(self, id ):
        self.rowId = id 
        
    def setColumnId(self, id ):
        self.columnId = id 
        
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
        #print json.dumps( self.page, cls=ObjectEncoder, indent=2, sort_keys=False)
        return json.dumps( self.page, cls=ObjectEncoder, indent=2, sort_keys=False)


class Footer:
    def __init__( self ):
        self.copyrightText = "Powered by <a href=\"https://github.com/ma-ha/rest-web-ui\">'Portal NG' {{PONGVER}}</a>, &copy; 2016, MH."
        self.linkList = [ { "text":"About", "url": "index.html?layout=about"} ]
        self.modules = [ { "id": "feedbackView", "type": "pong-feedback", "param": { } } ]
