import http.cookiejar
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

# def GetIdList():

def savefile(data,file_No):
    savepath = "D:\\spider\\"
    f_obj = open(savepath+str(file_No)+".html",'wb')
    f_obj.write(data)
    f_obj.close()



#登录验证页面
url = 'http://85.16.17.10/logincheck.php'
#手动添加js location 重定向后获取新闻的页面
url2 = 'http://85.16.17.10/portal/hnws/'
#新闻页面链接
url3 = 'http://85.16.17.10/general/news/show/read_news.php?NEWS_ID='
#附件
url4 = 'http://85.16.17.10/module/quick_preview/?AID=15248&MODULE=news&YM=1711&ATTACHMENT_ID=1847548138&ATTACHMENT_NAME=2017%C4%EA11%D4%C217%C8%D5%283852%29%A1%B6%C3%BF%C8%D5%CC%A8%C7%E9%A1%B7.doc&OP_CODE=a4175Ru7FGeYHUTdPlXL%2Fcl9enBAOxFrB40Asz%2B2'
#文件保存
file_No = 1

#账号密码设置
values = {'UNAME':'zhaozhao',
          'PASSWORD':'123456',
          'submit':'登 录'}
#伪造报头
webheader = {'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER',
             'Connection':'keep-alive',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
             'Accept-Encoding':'gzip, deflate',
             'Accept-Language':'zh-CN,zh;q=0.8',
             'Host':'85.16.17.10'
            }
# 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = http.cookiejar.LWPCookieJar()

cookie_support = urllib.request.HTTPCookieProcessor(cj)

opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)

urllib.request.install_opener(opener)


#构造编码登录信息
postDict = urllib.parse.urlencode(values).encode()

#发送登录信息到登录页面，获取对应的cookie
webpage = urllib.request.urlopen(url,postDict)
# request = urllib.request(url,values)
# response = urllib.urlopen(request)
#
webpage2 = urllib.request.urlopen(url2)
data2 = webpage2.read()
savefile(data2,file_No)
file_No = file_No + 1
print("主页获取完成")

webpage3 = urllib.request.urlopen(url3+'18917')
data3 = webpage3.read()
savefile(data3,file_No)
file_No = file_No + 1
print("新闻获取完成")
#简单办法抓取附件word
webpage4 = urllib.request.urlopen(url4)
data4 = webpage4.read()
savefile(data4,file_No)
file_No = file_No + 1
print(data4)


#解析获取内容data2
soup = BeautifulSoup(data2,'html.parser',from_encoding='utf-8')
#清理多余的格式
[script.extract() for script in soup.findAll('script')]
[style.extract() for style in soup.findAll('style')]
Contents = soup.find_all('p')
for content in Contents:
    Save_data = content.prettify(formatter='html')
    savefile(Save_data,file_No)
    file_No = file_No +1