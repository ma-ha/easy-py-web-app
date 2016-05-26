from webtest import TestApp
from nose.tools import *
from easywebapp.webapp import Portal 

class TestPortal():

    def setup( self ):
        middleware = []
        portal = Portal( 8000, { 'title':'Test' } )
        self.testApp = TestApp( portal.getApp().wsgifunc(*middleware) )
        
    def test_index(self):   
        r = self.testApp.get('/')
        assert_equal( r.status, '200 OK' )
        r.mustcontain('portal-ng.js')

    def test_layout_main(self):   
        r = self.testApp.get('/svc/layout/main')
        assert_equal( r.status, '200 OK' )
        r.mustcontain('layout')
        r.mustcontain('header')
        r.mustcontain('row')
        r.mustcontain('footer')
