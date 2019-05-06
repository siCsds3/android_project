
import codecs
from bs4 import BeautifulSoup

f = codecs.open("div.html", 'r', 'utf-8')
document = BeautifulSoup(f.read(),'html.parser')
print(document)

