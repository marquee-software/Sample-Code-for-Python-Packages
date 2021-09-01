import urllib                           # urllib is a package that collects several modules for working with URLs
import urllib.request
from bs4 import BeautifulSoup           # Beautiful Soup is a Python library for pulling data out of HTML and XML files.
# webpage 
theurl = "https://twitter.com/MarqueeSoftware"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")
# VSCode with Github
#print(soup.prettify())
print (soup.findAll('a'))
for link in soup.findAll('a'):
    print (link.get('href'))
print (soup.find('div',{"class":"ProfileHeaderCard"}))
