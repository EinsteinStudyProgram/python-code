from suds.client import Client
import xml.dom.minidom

url='http://apitest.wintalent.cn:8080/wt/xwebservices/externalResumeService?wsdl'
read_candidate = Client(url)
conditionXml='''
<?xml version="1.0" encoding="UTF-8"?>
<Condition>
	<corpCode><![CDATA[hntvhr]]></corpCode>
	<userName><![CDATA[hntvhr]]></userName>
	<password><![CDATA[aSfp8pL8U6MnKQrx]]></password>
<resumeType><![CDATA[2]]></resumeType>
	<currentPage><![CDATA[1]]></currentPage> 
	<rowSize><![CDATA[10]]></rowSize>
	<cType><![CDATA[1]]></cType>
</Condition>'''
try:
    get_condidate_xml = read_candidate.service.readEntryInformation(conditionXml)
except IOError as e:
    print(e.strerror)

doc_save = xml.dom.minidom.parseString(get_condidate_xml)

print(doc_save)

fp = open('candidate.xml', 'w')
doc_save.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="gb2312")
fp.close()