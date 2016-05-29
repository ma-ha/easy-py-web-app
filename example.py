# Copyright (c) 2016 ma-ha, The MIT License (MIT)
from easywebapp.webapp import Portal 
import easywebapp.page_layout as page

mainpage = page.PageLayout( 'First Page' )
mainpage.getRows().addView( page.View( 'View2', 'View 2', 'none' ), '200px' )
col_row = mainpage.getRows().addColumnsRow( 'row3', '200px' )
col_row.addView( page.View( 'Col 1', 'Col 1', 'none' ), '50%' )
col_row.addView( page.View( 'Col 2', 'Col 2', 'none' ), '50%' )

# initialize portal
portal = Portal( 'My Portal', 8000, mainpage )

# define a custom web service 
portal.addURL( '/myservice', 'myservice' )

class myservice:
    def GET( self ):
        return 'Hello World'

# start the web server
portal.run()