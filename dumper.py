import web
        
urls = (
    '/dump', 'dump'
)
app = web.application(urls, globals())

class dump:        
    def GET(self):

    	input = web.input()
    	# if input.password == "mysql-dumper":
    	if input.password =="mysql-dumper":
    		return "dumping..."
    	# 	return "dumping..."
    	# else:
    	return "Authorization Failed."

if __name__ == "__main__":
    app.run()
