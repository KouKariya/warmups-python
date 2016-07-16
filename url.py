import urllib2
url = "http://www.smogon.com" #Random site to test code
website = urllib2.urlopen(url)
print website.read()
