#url.py by Jesse Gallarzo
#Original source for code can be found at: https://www.hackthissite.org/articles/read/1053/
#Following code uses Python 2.7

import urllib2
url = "http://www.smogon.com" #Random site to test code
website = urllib2.urlopen(url)
print website.read() #lookup .read()
