#coding:utf-8
import urllib.request
import chardet
def parsering(url):
    req=urllib.request.Request(url)
    req.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/57.0')
    try:
        html=urllib.request.urlopen(req).read()
    except:
        print ("check the url")
    return checkdecode(html)
def checkdecode(html):
    if chardet.detect(html)["encoding"]=="utf-8":
        html=html.decode("utf8")
    else:
        html=html.decode("gbk")
    return html