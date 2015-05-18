#/usr/bin/python
#filename:python_reptile.py
import httplib2 as hl2
from html.parser import HTMLParser
def getData(link,name):
    global h
    response,content=h.request(link)
    pathfile='D:\\Python34\\fun\\'+name+".html"
    print(pathfile)
    with open(pathfile,'bw') as file:
        file.write(content)
class myHTMLParser(HTMLParser):   
    def __init__(self):
        HTMLParser.__init__(self)
        self.i=0
        self.falg=True
        self.out_tag=None
        self.tag=None
        self.link=None
        self.name=None
   #处理开始标签
    def handle_starttag(self,tag,attrs):
        if tag=="ul" and attrs.__contains__(('class','uk-nav uk-nav-side')) and self.falg:
            self.out_tag='start'
        if self.out_tag=="start" and tag=="a":
            self.tag="link"
            self.link="http://www.liaoxuefeng.com"+dict(attrs)["href"]
            print(self.link)

    #处理<></>之间的数据
    def handle_data(self,data):
        if self.tag=="link" and self.out_tag=="start" and self.link is not None:
            if data.__contains__(r"/"):
                data=data.replace(r"/",'_')   #避开'/'
            self.name=data
            print('name---',self.name)
            getData(self.link,self.name)
            if data=='期末总结':                
                self.out_tag=None
                self.falg=False       
            self.link=None
if __name__=="__main__":
    h=hl2.Http('.cache')
    response,content=h.request("http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000")
    m=myHTMLParser() 
    c=content.decode(encoding='utf-8')
    m.feed(c)
    m.close()
