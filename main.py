import web
import page_layout as page

render = web.template.render('templates/')

layout = page.Layout()
print 'INDENT:', layout.to_JSON()   

urls = (
    '/', 'index',
    '^/svc/layout/(.*)', 'layout'
#    '^/$', 'greet',
#    '/(.*)', 'index',
#    '^/about[/]?$', 'do_about'
)
app = web.application( urls, globals() )


class index:
    def GET( self ):
        return render.index()
 
class layout:
    def GET( self, x ):
        print 'in structure: '+x
        web.header('Content-Type', 'application/json')
        layout = page.Layout()
        return '{"layout":'+ layout.to_JSON() +'}' 

if __name__ == "__main__":
    print 'Startup...'
    app.run()
