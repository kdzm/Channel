import requests
import string
import re
list=["1091450","1929868","11735834","4417151","6837959","70155","4470554","82997","7332534","5296831","5530373","4327048","127343","11346757","4470554","20768","818274","3134673","2769289","4204573"]
headers_dicts={"ACCEPT":"application/json,application/xml,text/html","Content-Type":"application/x-www-form-urlencoded","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
post_data=''
post_data=post_data.encode('utf-8')
"""ACCEPT: application/json,application/xml,text/html
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
"""
for id in list:
    url_request="http://live.bilibili.com/api/playurl?player=1&quality=0&platform=android&otype=json&cid="+id
    #request_obj=requests.Request(url=url_request,data=post_data,headers=headers_dicts)
    txt=requests.post(url_request,post_data,headers=headers_dicts)
    txt.encoding = 'utf-8'
    txt1 = txt.text
    #print(txt1)
    n1=txt1.find('url":"')+len('url":"')
    n2=txt1.find('","',n1)
    url=txt1[n1:n2]
    playurl=url.replace("\\","")
    #if id=="70155":
        #print(txt1)
    print(id,playurl)
    #rdota2.encoding = 'utf-8'
    #txtdota2 = rdota2.text
#http://txy.live-play.acgvideo.com/live-txy/434730/live_27444411_4287972.flv?wsSecret=a7154b7bc1a26266c0d65e69a3158e2d&wsTime=1554173119&trid=d85a3c92c4c44e68932c03f95a8d41fd&sig=no
#User-Agent: Bilibili Freedoooooom/MarkII
