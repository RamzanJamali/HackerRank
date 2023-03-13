from docx import *
document = open('mbox_short.docx')
#words = document.xpath('//w:r', namespaces=document.nsmap)
WPML_URI = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
tag_rPr = WPML_URI + 'rPr'
tag_highlight = WPML_URI + 'highlight'
tag_val = WPML_URI + 'val'
tag_t = WPML_URI + 't'
for word in document:
    for rPr in word.findall(tag_rPr):
        high=rPr.findall(tag_highlight)
        for hi in high:
            if hi.attrib[tag_val] == 'yellow':
                print(word.find(tag_t).text.encode('utf-8').lower())
