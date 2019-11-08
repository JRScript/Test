import urllib3
import html2text
import requests
import shutil
import re
from bs4 import BeautifulSoup
def border():
    url1 = ("https://helpx.adobe.com/in/security/products/adm/apsb19-56.html")
    http = urllib3.PoolManager()
    r = http.request ("GET", url1)
    result = int (r.status)
    if result == 200:
        r = requests.get (url1)
        soup = BeautifulSoup(r.content)
        soup2 = str(soup.encode("utf-8"))
        print (soup2)
        doc = open('html.txt', "w+")
        doc.write (soup2)
        doc.close()
    elif result == 404:
        print ("Page Not Found")

border()
