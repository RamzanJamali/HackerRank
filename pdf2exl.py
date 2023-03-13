import PyPDF2
import xlwt
from xlwt import Workbook as wb
import re
import io
workbook = xlwt.Workbook()  
sheet = workbook.add_sheet("Sheet Name")

pdfFileObj = open('emp.pdf', 'rb')  
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

emails = []
num_pages = pdfReader.numPages
for i in range(num_pages):
    pageObj = pdfReader.getPage(i)
    page = pageObj.extractText()
    page = page.split()
    for mail in page:
        x = re.findall('[^0-9]+@\S+', mail)
        if not x: continue
        y = re.split('LACITY.ORG', x[0])
        emails.append(y[0]+'LACITY.ORG')


sheet.write(0, 0, 'EMAIL')
b = 0
for email in emails:
    b = b + 1
    sheet.write(b, 0, email.lower())
workbook.save("emp.xls")
