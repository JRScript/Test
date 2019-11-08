import pandas as pd
from openpyxl import *
import os
import sys

url = ("https://helpx.adobe.com/in/security/products/" * "/apsb19-50.html")

cwd = os.getcwd()

writer = pd.ExcelWriter("Demo.xlsx")

table = pd.read_html(url)[0]
table1 = pd.read_html(url)[1]
table2 = pd.read_html(url)[2]
table3 = pd.read_html(url)[3]
	
table.to_excel(writer, startrow=0, index=False)
writer.save()
table1.to_excel(writer, startrow=4, index=False)
writer.save()
table2.to_excel(writer, startrow=8, index=False)
writer.save()
table3.to_excel(writer, startrow=12, index=False)
writer.save()

try:
	table3 = pd.read_html(url)[4]
except:
	pass
