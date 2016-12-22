import web
        
urls = (
    '/dump', 'dump'
)
app = web.application(urls, globals())

class dump:        
    def GET(self):
        return "dumping" 

if __name__ == "__main__":
    app.run()
