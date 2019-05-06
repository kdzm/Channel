
import requests
import string
hunanTV={"280":"湖南经视","346":"湖南都市","344":"湖南娱乐","287":"金鹰卡通","316":"金鹰纪实","229":"国际频道","484":"湖南电视剧","261":"湖南公共","329":"先锋乒羽","578":"茶频道","218":"快乐垂钓"}
"""  -频道ID
280湖南经视
346湖南都市
344湖南娱乐
287金鹰卡通
316金鹰纪实
229国际频道
484湖南电视剧
261湖南公共
329先锋乒羽
578茶频道
218快乐垂钓
"""
ID=hunanTV.keys()
#name=hunanTV.values()
for x in ID:
    url="https://mpplive.api.mgtv.com/v1/epg/turnplay/getLivePlayUrlMPP?version=PCweb_1.0&platform=4&buss_id=2000001&channel_id="+x+"&definition=std&_support=10000000"
    headers={"":""}
    r=requests.get(url)
    """
    方法1：使用r.content，得到的是bytes型，再转为str
    html=r.content
    html_doc=str(html,'utf-8')
    print(html_doc)
    """
    #使用r.text
    r.encoding='utf-8'
    txt=r.text
    print(x,hunanTV[x])
    n1=txt.index("http")
    #print(n1)
    n2=txt.index("flv")+len("flv")
    #print(n2)
    url1=txt[n1:n2]
    #print(url1)
    #url.translate(str.maketrans('', '', string.punctuation))
    #playurl=url.translate(str.maketrans(",,", string.punctuation))
    #print str1.index(str2, 2);#结果5
    #print(txt)
    playurl=url1.replace(",,","")
    print(playurl+"\n")
    with open('HunanTV.htm','a+',encoding="utf-8") as f:f.write(hunanTV[x]+":"+playurl+"\n")
    #with open('HunanTV.txt', 'a+', encoding="utf-8") as f: f.write(hunanTV[x]+":"+playurl+"\n")