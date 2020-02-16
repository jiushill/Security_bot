#@author:九世
#@time:2019/12/11
#@file:main.py

from gevent import monkey;monkey.patch_all()
from multiprocessing import Process
from colorama import Fore,init
from bs4 import BeautifulSoup
import gevent
import feedparser
import asyncio
import requests
import re
import os
import socket
socket.setdefaulttimeout(5)

jgs=[]

init(wrap=True)
class Rss_zhuaqu(object):
    def __init__(self,files,id):
        self.dicts={}
        dk=open('rss.txt','r',encoding='utf-8')
        for d in dk.readlines():
            dv="".join(d.split('\n')).split('>')
            self.dicts[dv[0]]=dv[1]
        dk.close()
        self.headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
        self.ybs=[]
        self.djcs=[]
        self.xcs=[]
        self.calc=0
        self.calc2=0
        self.fbg=[]
        self.file=files
        self.id=id

    def rdfiles(self):
        dk=open('db.txt','r',encoding='utf-8')
        for r in dk.readlines():
            data="".join(r.split('\n'))
            yield data

    def loads(self):
        for u in self.rdfiles():
            self.fbg.append(u)

    def fds(self,datas):
        if self.id == 1:
            print(datas)
            print(datas, file=open(self.file, 'a', encoding='utf-8'))
        else:
            self.rdfiles()
            self.loads()
            if datas not in self.fbg:
                print(datas)
                print(datas, file=open('save.txt', 'a', encoding='utf-8'))
                print(datas, file=open('db.txt', 'a', encoding='utf-8'))
            else:
                print('[-] 没有新的动态')

    def zhua(self,url):
        id=list(self.dicts.keys())[list(self.dicts.values()).index(url)]
        try:
            d = feedparser.parse(url)
            if 'syntax error' in str(d):
                rqt = requests.get(url=url, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Mobile Safari/537.36'},timeout=3)
                text = BeautifulSoup(rqt.text, 'html.parser')
                for y in text.find_all('item'):
                    title = BeautifulSoup(str(y), 'html.parser').find_all('title')
                    link = re.findall('[a-zA-z]+://[^\s]*<', str(y))
                    datas = 'title:{} link:{} id:{}'.format(title[0].get_text(), str(link[0]).replace('<', ''),id)
                    self.fds(datas)
            else:
                for u in d['entries']:
                        datas='title:{} value:{} id:{}'.format(u['title'],u['link'],id)
                        self.fds(datas)

        except Exception as r:
            print(Fore.RED+'[-] '+Fore.WHITE+'Error:{}'.format(r))


    def xc(self,rw):
        for c in rw:
            self.xcs.append(gevent.spawn(self.zhua,c))
        
        gevent.joinall(self.xcs)
        self.xcs.clear()

    def djc(self):
        for u in self.ybs:
            if self.calc2==100:
                p=Process(target=self.xc,args=(self.djcs,))
                p.start()
                self.calc2=0
                self.djcs.clear()
                p.join()

            self.djcs.append(u)
            self.calc2+=1

        if len(self.djcs)>0:
            p = Process(target=self.xc, args=(self.djcs,))
            p.start()
            self.calc2 = 0
            self.djcs.clear()
            p.join()

    async def main(self):
        for j in self.dicts:
            if self.calc==100:
                self.djc()
                self.ybs.clear()
                self.calc=0

            self.ybs.append(self.dicts[j])
            self.calc+=1

        if len(self.ybs)>0:
            self.djc()
            self.ybs.clear()
            self.calc = 0


if __name__ == '__main__':
    if os.path.exists('save.txt'):
        a = open('save.txt', 'w', encoding='utf-8')
        a.close()
        file = 'save.txt'
        id = 0
    else:
        a = open('save.txt', 'w', encoding='utf-8')
        a.close()
        file = 'db.txt'
        id = 1

    obj = Rss_zhuaqu(file, id)
    loop = asyncio.get_event_loop()
    tk = loop.create_task(obj.main())
    loop.run_until_complete(tk)
