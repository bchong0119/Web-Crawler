#! usr/bin/env python2.7 

import sys 
import os
import requests
from requests.exceptions import ConnectionError
import networkx as nx
import matplotlib.pyplot as plt

def usage(status=0):
    print '''Usage: webcrawler.py <URL> <Depth desired>'''
    return status

def convertURL(url):
    '''takes url and makes sure it starts with http://'''
    if url.startswith('http://') or url.startswith('https://'):
        return url
    elif url.startswith('www.'):
    	return 'http://'+url
    elif not url.startswith('http://') or not url.startswith('https://'):
        return 'http://'+url
    return url

def crawl(numlinks, url):
    '''Crawls a website starting with input url and stores the data into LINKS. Will crawl for a depth of numlinks'''

    LINKS={} 

    url=convertURL(url)

    for i in range(0,numlinks):
	if i==0:   #initialize dictionary
	    site=requests.get(url)
	    LINKS[url]=set()
	    for line in site.text.split('"'):
		if line.startswith('http://') or line.startswith('https://'):
		    LINKS[url].add(line)
	else:
	    #make separate list of keys so that we do not loop extra times because we added to dict
	    linkkeys=LINKS.keys()

	    for key in linkkeys:
		for URL in LINKS[key]:
		    #make sure URL is in correct format 
		    convertURL(URL)

		    #check to make sure it isnt already a key to prevent infinite loops
		    #duplicates not included on graph
		    if URL in linkkeys:
		        continue

		    try:	
			#check if website exists
			site=requests.get(URL)

			if site.status_code != 200:
			    print URL, "website cannot be accessed!"
			    #sys.exit()
			    continue
		    except ConnectionError:
			print URL, "website cannot be accessed!"
			continue
	    

		    #add that website as a key and follow all links to that 
		    LINKS[URL]=set()

		    for line in site.text.split('"'):
			if line.startswith('http://') or line.startswith('https://'): 
			    LINKS[URL].add(line)
    return LINKS 

def creategraph(LINKS):
    #initialize a graph
    G=nx.Graph()
    
    #iterate through LINKS to add nodes and edges 
    for key, value in LINKS.items():
	G.add_node(key)
	for item in value:
	    G.add_node(item)
	    G.add_edge(key, item)
    
    nx.draw_spring(G,arrows=False,with_labels=False,node_size=50,node_color='green',font_size=8)
    plt.savefig("graph.png")
    os.system("convert graph.png -resize 130% graph.jpg")

if __name__ == "__main__":

    #read in url and depth from command line
    if len(sys.argv)<=1:
        usage()
	sys.exit("No arguments in command line")

    URL=sys.argv[1]
    numlinks=sys.argv[2]

    #dictionary that contains what websites link to what
    LINKS={}

    #Read in website name from user
    #URL=raw_input("What website would you like to crawl? ")
    #numlinks=raw_input("How deep would you like to crawl? Enter a positive integer number greater than 0: ")

    #check that numlinks is valid 
    if numlinks<=0:
        print "You must enter a number greater than 0 for depth"
	sys.exit()

    #check that url starts with http
    URL=convertURL(URL)

    try:
	#check if website exists
	site=requests.get(URL)

	if site.status_code != 200:
	    print "website cannot be accessed!"
	    sys.exit()

    except ConnectionError:
    	print URL, "website cannot be accessed!"
	sys.exit()

    #if it does exists, parse html results to find urls, add then to dict
    #going through main website user gave
    #go to each website and find what links are in those
    LINKS=crawl(int(numlinks), URL)


    #with open("links.txt", "w") as f:
#	for key, value in LINKS.items():
#	     f.write(">>>"+key)
#	    for v in value:	
#		f.write(v)

    #create graph visualization 
    creategraph(LINKS)
