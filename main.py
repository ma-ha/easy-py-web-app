# Copyright (c) 2016 ma-ha, The MIT License (MIT)
import webapp

# initialze portal
portal = webapp.Portal( { 'title':'Test' } )

# define a custom web service 
portal.addURL( '/myservice', 'myservice' )

class myservice:
    def GET( self ):
        return 'Hello World'

# start the web server
portal.run()