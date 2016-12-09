# Web-Crawler
Borah Chong
12/09/2016

The purpose of this program is to run through a website to look for links, also known as a web crawler. It follows those links to look for other links that the website is connected to and creates a graph. 

The file that has the code for the actual web crawling is called "webcrawler.py". This program produces a png and jpg of the graph generated. The file called "page.py" is the file that can be run to start the website. The "main.html" and the "graph.html" files are the html code used to display the web page. 

This program can be run either in the terminal or through a website. It is written in Python using the Tornado software to create the webpage, and also uses Bootstrap for personalization and theme. To set up the website, simply run "python page.py" and the website will run. The current port number is 9092. To just run the crawl program without having to run the website, run "python webcrawler.py <url> <depth>" where the url is the start web page to search links for, and the depth is the number of links in that we look. The minimum for depth is 1, which means looking for only the links on the url give. If depth were 2, the program would look at the links on the given url, and would also continue looking for links on those that were on the given url.

This repository is organized into two folders, INFO and CODE. The CODE folder has the source code for the program. The INFO folder has information about requirements and contributors. 
