import urllib
import urllib.request
from bs4 import BeautifulSoup


theurl = "https://twitter.com/MarqueeSoftware"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")

# Testing VSCode with Github

#print(soup.prettify())
print (soup.findAll('a'))
for link in soup.findAll('a'):
    print (link.get('href'))
print (soup.find('div',{"class":"ProfileHeaderCard"}))
