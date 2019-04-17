import requests
def geturl(url,headers):
    r=requests.get(url,headers=headers)
    r.encoding='utf-8'
    #r.encoding='GB2312'
    r=r.text
    #print(r)
    return r