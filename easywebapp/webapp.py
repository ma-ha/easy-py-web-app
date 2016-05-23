# Copyright (c) 2016 ma-ha, The MIT License (MIT)
import web
import page_layout as page

render = web.template.render('templates/')

class Portal:
    pages = []
    urls = (
        '/', 'index',
        '^/svc/layout/(.*)', 'layout'
    )

    def __init__( self, main_page ):
        self.pages.append( main_page )
        self.app = web.application( self.urls, globals() )
        
    def addURL(self, url_pattern, url_class ):
        self.urls = self.urls + ( url_pattern, url_class )    
        
    def run(self):    
        print 'Startup...'
        self.app.run()


class index:
    def GET( self ):
        return render.index()
 
class layout:
    def GET( self, x ):
        print 'in structure: '+x
        web.header('Content-Type', 'application/json')
        layout = page.Layout()
        return '{"layout":'+ layout.to_JSON() +'}' 
