from suds.client import Client
import xml.dom.minidom
import time

url='http://apitest.wintalent.cn:8080/wt/xwebservices/externalResumeService?wsdl'
read_candidate = Client(url)


try:
    for i in range(1,11):
        pagenumber=i
        conditionXml = '''
        <?xml version="1.0" encoding="UTF-8"?>
        <Condition>
            <corpCode><![CDATA[hntvhr]]></corpCode>
            <userName><![CDATA[hntvhr]]></userName>
            <password><![CDATA[aSfp8pL8U6MnKQrx]]></password>
            <resumeType><![CDATA[2]]></resumeType>
            <currentPage><![CDATA[%s]]></currentPage> 
            <rowSize><![CDATA[10]]></rowSize>
            <cType><![CDATA[1]]></cType>
        </Condition>'''%(pagenumber)
        get_condidate_xml = read_candidate.service.readEntryInformation(conditionXml)
        print(get_condidate_xml)
        doc_to_xml = xml.dom.minidom.parseString(get_condidate_xml)
        print(conditionXml)
        filename = "candidate-%s.xml" % (pagenumber)
        fp = open(filename, 'w')
        doc_save = doc_to_xml.toprettyxml(indent="\t", newl="\n", encoding="gbk")
        doc_save =bytes.decode(doc_save,encoding="gbk")
        fp.write(doc_save)
        # doc_save.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="Unicode")
        fp.close()
except IOError as e:
    print(e.strerror)


