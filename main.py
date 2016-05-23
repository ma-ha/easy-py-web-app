# Copyright (c) 2016 ma-ha, The MIT License (MIT)
from easywebapp.webapp import Portal 

# initialze portal
portal = Portal( { 'title':'Test' } )

# define a custom web service 
portal.addURL( '/myservice', 'myservice' )

class myservice:
    def GET( self ):
        return 'Hello World'

# start the web server
portal.run()