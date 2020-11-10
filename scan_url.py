# python3
#-*- coding:utf-8 _*-
"""
@author:Administrator
@file: scan_url.py
@time: 2020/07/07
"""

'''
自己写的扫描路径
'''
import requests
import time
import queue
import threading



headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'PHPSESSID=20ntjr40v0kbmml3p3lf0fuq50; __q__=1592665366780',
    'Connection': 'close',
    'Content-Length': '14'
}
headers2 = {
    'User-Agent':'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
}

# 读取文件
def readlocat(paht_name):
    idsip = []
    lenint=0
    rfile5 = open(paht_name)
    for line in rfile5.readlines():
        linen = line.strip('\n')
        idsip.append(linen)
        lenint=lenint+1
    return idsip,lenint
def writendata(data):
    w = open('url200.txt','a',encoding='utf-8')
    w.write(data+'\n')
    w.close()

#线程传输
def main():

    #print('dicc#',dicc)

    for d in dicc:
        u=url+d
        try:
            print(u)
            re=requests.get(url=u,headers=headers2)
            cod=re.status_code
            #print(cod)
            uu = u + '|' + str(cod)
            print('type',type(cod))
            if cod==200:
                print(uu)
                writendata(uu)
            else:
                writendata(uu)
        except:
            print('connext excepts')
            pass
        time.sleep(0.5)




def mainthr():
    while not q.empty():
        i = q.get()
        print('读取当前,当前', i, lendd)

        u = url +dicc[i]
        print(u)
        print(time.asctime(time.localtime(time.time())))
        try:

            re = requests.get(url=u, headers=headers2)
            cod = re.status_code
            UU=u+' | '+str(cod)

            print(UU)
            if cod == 200:
                writendata(UU)
            else:
                pass
        except:
            print('connext excepts')
            pass
        print(time.asctime(time.localtime(time.time())))
        time.sleep(0.5)




if __name__=='__main__':
    url = 'http://www.***.com/'
    paht = 'config\\ASP.txt'
    dicc,lendd= readlocat(paht)
    print(lendd)
    q=queue.Queue()
    for i in range(0,lendd):
        q.put(i)

    #开启几个线程扫描
    for t in range(1):
        thr=threading.Thread(target=mainthr)
        thr.start()
        time.sleep(0.5)
    #main()