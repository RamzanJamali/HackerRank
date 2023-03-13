import PyPDF2
import re

pdfFileObj = open('emp.pdf', 'rb')  
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

names = []
num_pages = pdfReader.numPages
for i in range(num_pages):
    pageObj = pdfReader.getPage(i)
    page = pageObj.extractText()
    page = page.split('\n')
    for name in page:
        x = re.findall('[a-zA-Z]+,\s[a-zA-Z]+', name)
        if not x: continue
        for z in x:
            y = re.split(',', z)
            names.append(y[1])

#print(names)
