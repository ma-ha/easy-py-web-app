# Copyright (c) 2016 ma-ha, The MIT License (MIT)
from easywebapp.webapp import Portal 
import easywebapp.page_layout as page

mainpage = page.PageLayout()

# initialze portal
portal = Portal( 8000, mainpage )

# define a custom web service 
portal.addURL( '/myservice', 'myservice' )

class myservice:
    def GET( self ):
        return 'Hello World'

# start the web server
portal.run()