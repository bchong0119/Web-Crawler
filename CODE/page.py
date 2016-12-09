#! usr/bin/env python2.7

import tornado.ioloop
import tornado.web
import os
import webcrawler

PORT=9092

class MainHandler(tornado.web.RequestHandler):
    '''creates main page of website'''
    def get(self):
       self.render('main.html')
    	

class GraphHandler(tornado.web.RequestHandler):
    '''displays graph to user and displays list of links below image'''
    def get(self):
        url = self.get_argument('url', '')
	depth=self.get_argument('numlinks', 1)

	#pass arguments to webcrawler function
	LINKS={}
	LINKS=webcrawler.crawl(int(depth), url)
	webcrawler.creategraph(LINKS)
        
	#display graph created by function
	self.render("graph.html", url=url, depth=depth, links=LINKS)

def makeApp():
    return tornado.web.Application([
	(r"/", MainHandler), 
	(r"/graph", GraphHandler),
	(r"/(graph.jpg)", tornado.web.StaticFileHandler, {'path': '.'}),
    ], debug = True)


if __name__=="__main__":
    app=makeApp()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
    #Application.listen(PORT)

