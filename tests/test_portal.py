from webtest import TestApp
from nose.tools import *
from easywebapp.webapp import Portal 
import easywebapp.page_layout as page

class TestPortal():

    def setup( self ):
        middleware = []
        self.mainpage = page.PageLayout( 'First Page' )
        self.portal = Portal( 'My Portal', 8000, self.mainpage )
        self.testApp = TestApp( self.portal.getApp().wsgifunc( *middleware ) )
        
    def test_index(self):   
        r = self.testApp.get( '/' )
        assert_equal( r.status, '200 OK' )
        r.mustcontain( 'portal-ng.js' )

    def test_layout_main(self):   
        r = self.testApp.get( '/svc/layout/main/structure' )
        assert_equal( r.status, '200 OK' )
        r.mustcontain('layout')
        r.mustcontain('header')
        r.mustcontain('row')
        r.mustcontain('footer')

    def test_add_view(self):   
        self.mainpage.getRows().addView( page.View( 'View2', 'View 2', 'none' ), '400px' )
        r = self.testApp.get( '/svc/layout/main/structure' )
        assert_equal( r.status, '200 OK' )
        r.mustcontain('View 1')
        r.mustcontain('View 2')

    def test_add_coomplex_layout(self):   
        col_row = self.mainpage.getRows().addColumnsRow( 'row3', '200px' )
        col_row.addView( page.View( 'Col 1', 'Col 1', 'none' ), '30%' )
        col_row.addView( page.View( 'Col 2', 'Col 2', 'none' ), '30%' )
        row = col_row.addRowsColumn( 'Col 3', '40%' )
        row.addView( page.View( 'C3 R1', 'C3 R1', 'none' ), '100px'  )
        row.addView( page.View( 'C3 R2', 'C3 R2', 'none' ), '100px'  )

        r = self.testApp.get( '/svc/layout/main/structure' )
        assert_equal( r.status, '200 OK' )
        r.mustcontain('Col 1')
        r.mustcontain('Col 1')
        r.mustcontain('C3 R1')
        r.mustcontain('C3 R2')
