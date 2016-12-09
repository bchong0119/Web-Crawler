#! usr/bin/env python2.7

#goes through a list of websites and tests them with webcrawler.py for depths from 1 to 3
#writes data to results.txt file

import sys
import os
import subprocess

TEST=['facebook.com', 'google.com', 'nd.edu']

for link in TEST:
    print "---testing website: {}".format(link)
    os.system("echo '-----{}' >> results.txt".format(link))

    for i in range(1,4):
	print "testing for depth {}".format(i)
        os.system("echo '--depth of {}' >> results.txt".format(i))
	cmd="(time python bench-webcrawler.py {} {} ) 2>> results.txt".format(link, i)
	print cmd
	os.system(cmd)
    print 




