#coding:utf-8
import xml.etree.ElementTree as ET
#{'com': 'COM1', 'bsp': '115200', 'd': '8', 'p': 'NONE', 's': '1'}
def WriteXml(sl):
    root=ET.Element("com")
    for e in sl.keys():
        l=ET.SubElement(root,"set")
        l.attrib={'name':e,'value':sl[e]}
    tree = ET.ElementTree(root)
    tree.write("setmsg.xml")

def ReadXml(spath):
    root=ET.parse(spath)
    p=root.findall('.')
    xmllist={}
    for oneper in p:
        for child in oneper.getchildren():
            xmllist[child.attrib['name']]=child.attrib['value']
    return xmllist

#sl={'com': 'COM1', 'bsp': '115200', 'd': '8', 'p': 'NONE', 's': '1'}
#WriteXml(sl)
#spath="setmsg.xml"
#print(ReadXml(spath))