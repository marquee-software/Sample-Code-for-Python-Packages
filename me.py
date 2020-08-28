import urllib
import urllib.request
from bs4 import BeautifulSoup


theurl = "https://twitter.com/RanjSriv"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")

#print(soup.title.text)
#print (soup.findAll('a'))
#for link in soup.findAll('a'):
#    print (link.get('href'))
print (soup.find('div',{"class":"ProfileHeaderCard"}))