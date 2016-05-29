# Copyright (c) 2016 ma-ha, The MIT License (MIT)
from easywebapp.webapp import Portal 
import easywebapp.page_layout as page

mainpage = page.PageLayout( 'First Page' )

# lets add a WIKI content view 
view1 = page.View( 'WikiView', 'MediaWiki View', 'none' )
view1.setViewType( 'pong-mediawiki' )
view1.setResourceURL( 'http://${lang}.wikipedia.org/w/' )
view1.setViewConfig(
    { 'page': { 'EN': "Main_Page",
                'DE': "Wikipedia:Hauptseite",
                'IT': "Pagina_principale" },
      'wikiRef': "/wiki/" }
)
mainpage.getRows().addView( view1, '300px' )

# ... and now add some views in a "complex" layout
col_row = mainpage.getRows().addColumnsRow( 'row3', '200px' )
col_row.addView( page.View( 'Col 1', 'Col 1', 'none' ), '30%' )
col_row.addView( page.View( 'Col 2', 'Col 2', 'none' ), '30%' )
row = col_row.addRowsColumn( 'Col 3', '40%' )
row.addView( page.View( 'C3 R1', 'C3 R1', 'none' ), '100px'  )
row.addView( page.View( 'C3 R2', 'C3 R2', 'none' ), '100px'  )

# initialize portal
portal = Portal( 'My Portal', 8000, mainpage )

# define a custom web service 
# (that's not required here, just as an example)
portal.addURL( '/myservice', 'myservice' )

class myservice:
    def GET( self ):
        return 'Hello World'

# start the web server
portal.run()