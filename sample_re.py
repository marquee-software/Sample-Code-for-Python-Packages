import re
from bs4 import BeautifulSoup

#source_code = self.textInput.toHtml()
source_code =  """.......<p style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Ubuntu';">ABC ABC<br />ABC</span></p>.......""" 

soup = BeautifulSoup(source_code, "lxml")

'''
for elm in soup.find_all('span', style=re.compile(r"font-family:'Ubuntu'")):
#actually there was a for loop
#    elm.string = elm.text.replace("A", "X")
#    elm.string = elm.text.replace("B", "Y")
#    elm.string = elm.text.replace("C", "Z")
    for text in elm.find_all(text=True):
        text.replace_with(text.replace("A", "X").replace("B", "Y").replace("C", "Z"))
'''
for elm in soup.find_all('span', style=re.compile(r"font-family:'Ubuntu'")):
    replacements = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }
    for text in elm.find_all(text=True):
        text_to_replace = text
        for k, v in replacements.items():
            text_to_replace = text_to_replace.replace(k, v)

        text.replace_with(text_to_replace)
print(soup.prettify())