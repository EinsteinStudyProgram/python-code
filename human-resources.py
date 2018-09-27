from suds.client import Client
import xml.dom.minidom
import time

url='http://apitest.wintalent.cn:8080/wt/xwebservices/externalResumeService?wsdl'
read_candidate = Client(url)
pagenumber = 1
conditionXml='''
<?xml version="1.0" encoding="UTF-8"?>
<Condition>
	<corpCode><![CDATA[hntvhr]]></corpCode>
	<userName><![CDATA[hntvhr]]></userName>
	<password><![CDATA[aSfp8pL8U6MnKQrx]]></password>
<resumeType><![CDATA[2]]></resumeType>
	<currentPage><![CDATA[3]]></currentPage> 
	<rowSize><![CDATA[10]]></rowSize>
	<cType><![CDATA[1]]></cType>
</Condition>'''

try:
    for pagenumber in range(1,10):
        get_condidate_xml = read_candidate.service.readEntryInformation(conditionXml)
        doc_save = xml.dom.minidom.parseString(get_condidate_xml)
        filename = "candidate-%s.xml" % (pagenumber)
        fp = open(filename, 'w')
        doc_save.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="gb2312")
        fp.close()
except IOError as e:
    print(e.strerror)


print(doc_save)

