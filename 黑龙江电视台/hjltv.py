import requests
import string
import re
hljtvid={"黑龙江导视":"2","黑龙江卫视":"3","黑龙江都市":"4","黑龙江公共":"5","黑龙江农垦":"6","黑龙江少儿":"7","黑龙江文体":"8","黑龙江新闻":"9","黑龙江影视":"10"}
#hljtvid={"黑龙江导视":"2"}
name=hljtvid.keys()
id=hljtvid.values()
request_url1="http://www.hljtv.com/m2o/channel/channel_info.php?id="
request_url2="http://www.hljtv.com/m2o/program_switch.php?&shownums=6&channel_id="
request_url3="http://www.hljtv.com/m2o/player/program_xml.php?id=3&channel%5Fid=3&access%5Ftoken=&time="
headers={"Referer":"http://www.hljtv.com/live/folder424/","User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
for x in name:
    #url=request_url2 or request_url1 +hljtvid[x]
    url =request_url1 + hljtvid[x]
    r=requests.get(url,headers)
    r.encoding='utf-8'
    txt=r.text
    if txt.find("403")!=-1:
        r1=requests.get(request_url1+hljtvid[x], headers)
        r1.encoding = 'utf-8'
        txt=r1.text
    #print(txt)
    n1=txt.find('"m3u8":"')+len('"m3u8":"')
    n2=txt.find('","',n1)
    url=txt[n1:n2]
    playurl1=url.replace('\\',"")
    #http:// stream2.hljtv.com/hljws/playlist.m3u8?_upt =3a5a1c001554182315
    print(x,playurl1)
    #playurl1=playurl1.replace("http","m3u8")
    print(x,playurl1)
    #playurl要加头部    User-Agent: Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53
    #                   Referer: http://www.hljtv.com/live/folder424/
    #                   http://www.hljtv.com/m2o/player/channel_xml.php?first=1&url=http%3A%2F%2Fwww%2Ehljtv%2Ecom%2Flive%2Ffolder424%2F&id=9&access%5Ftoken=&extend=
    #ts1=requests.get(playurl1,headers)
    #ts1.encoding='utf-8'
    #ts2=ts1.text
    #print(ts2)