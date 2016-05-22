import json

class Header:
    def __init__( self, logo ):
        self.logoText = logo
        self.modules = [ ] 
        
class Footer:
    def __init__( self ):
        self.copyrightText = "Powered by <a href=\"https://github.com/ma-ha/rest-web-ui\">'Portal NG' {{PONGVER}}</a>, &copy; 2016, MH."
        self.linkList = [ { "text":"About", "url": "index.html?layout=about"} ]
        self.modules = [ { "id": "feedbackView", "type": "pong-feedback", "param": { } } ]       

class Layout:
    def __init__(self):
        self.title  = "New Portal"
        self.header = Header( "New Portal" )
        self.rows   = [ {"id":"Page1","rowId":"Page1","title":"Page 1","decor":"decor","resourceURL":"none","height":"400px"} ]
        self.footer  = Footer()

    def to_JSON(self):
        return json.dumps( self, default=lambda o: o.__dict__ )
