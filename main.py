# Copyright (c) 2016 ma-ha, The MIT License (MIT)
import webapp

portal = webapp.Portal( { 'title':'Test' } )

portal.addURL( '/nav', 'nav' )

portal.run()