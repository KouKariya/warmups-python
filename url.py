#url.py by Jesse Gallarzo
#Original source for code can be found at: https://www.hackthissite.org/articles/read/1053/
#Following code uses Python 2.7

import urllib2
import sys

url = str(sys.argv[1]) #1st arg is used as the website to run the script on
website = urllib2.urlopen(url)
print website.read() #lookup .read()
