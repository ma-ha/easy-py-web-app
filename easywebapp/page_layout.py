# Copyright (c) 2016 ma-ha, The MIT License (MIT)
import json

class Footer:
    def __init__( self ):
        self.copyrightText = "Powered by <a href=\"https://github.com/ma-ha/rest-web-ui\">'Portal NG' {{PONGVER}}</a>, &copy; 2016, MH."
        self.linkList = [ { "text":"About", "url": "index.html?layout=about"} ]
        self.modules = [ { "id": "feedbackView", "type": "pong-feedback", "param": { } } ]       

class PageLayout:
    portal = None
    page = {}
    def __init__( self ):
        self.page['title']  = 'New Portal'
        self.page['header'] = { 'logoText':'New Portal', 'modules':[] }
        self.page['rows']   = [ {"id":"Page1","rowId":"Page1","title":"Page 1","decor":"decor","resourceURL":"none","height":"400px"} ]
        self.page['footer']  = Footer()

    def addToPortal( self, portal ):
        self.portal = portal


    def to_JSON(self):
        if self.portal != None :
            self.page['title'] = self.portal.getTitle() 
            self.page['header'] = self.portal.getHeader()
        return json.dumps( self.page, default=lambda o: o.__dict__ )
