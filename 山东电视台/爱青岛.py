import time
from requestget import geturl
from MD5 import  get_token
import os
from DPL频道列表模板 import lists
headers={'User-Agent':'Dalvik/1.6.0 (Linux; U; Android 8.1.0; QABOX_1 Build/KOT49H)'}
channels={'QTV-1':'78243592032538624515160887874fd1319af774e3b885d6c1642b7c2744f1bb36d497e48e63221de13bc4b94203','QTV-2':'7824358725187092531516088768335a979d9f92cadf3d66d1a47b0d0b5bfe4b850cdc4401bd16721f085d219820','QTV-3':'7824358178837053491516088800c2a6e7471865d7f7ad0061dc708a5c89a5d0b21c8ce11f9052b4c9eee6b4bbcb','QTV-4':'782435770118971397151608881040ad7542ba8cfdcb49e3015076823fdf52fb1b9d8f96d82f661779492c35e79a','QTV-5':'7824357233608704051516088823a12573b94341d837f310b2fc333231793de5c0eba02494a57e198f481e5a52bc','QTV-6':'782435677038977029151608883491d373c6f493807262ba2b16c27e7e7dde8d63c06c2fda8ef60d951081d00985'}
playurls=[]
print(len('9f6542743738e4e4191ef2de0e5892a335e147303f43cf52844add9eea83f14e'))
t=str(int(time.time()))
sg='http://v2.91kds.cn/c9/sdqdtv.m3u8?id=sdqdtv4&app=org.jykds.tvlive&version=1.9.7&mac=ec:01:ee:17:ce:8a&nwtime='+t+'&ev=20180910'
sign=get_token(message=sg)
print(t,sign)
sg='http://egg.cluster.feiyunbox.com/key/iqd?key=qtv1at&v=3&tm='+t+'&sign='+sign
print(sg)
with open('QTV.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('QTV.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0'+'\n')
for x,y in channels.items():
    t=str(int(time.time()))
    #print(t)
    #device_id ='4438189f768ead5289109fb813c4b447'
    y1=str(y)
    y=str(y1[0:18])
    signature=get_token(message=y)
    y2=str(y1[18:28])
    y3=str(y1[28:])
    #print(y3)
    #print(y2)

    url='http://yingyong.aiqd.com.cn/api/v4/telecasts/channels/iqingdao?city_id=370200&uid=0&platform=2&nonce=123456&client_ver=5.0&device_id=9be5940516ad19bd1af87a81f04f32c2&client_id=370200&type=1&deviceId=9be5940516ad19bd1af87a81f04f32c2&timestamp='+y2+'&signature='+y3+'&channel_id='+y
    #print(url)
    r=geturl(url,headers=headers)
    #print(r)
    #a=True
    n1=r.find('],"play_url":"')+len('],"play_url":"')
    n2=r.find('"',n1)
    playurl=r[n1:n2]
    playurls.append(playurl)
names=list(channels.keys())
for u in playurls:
    j=playurls.index(u)
    (x,y)=lists(names[j],u)
    with open('QTV.dpl', 'a+', encoding="utf-8") as f: f.write(str(j+1)+x + "\n"+str(j+1)+y+"\n"+str(j+1)+'*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\山东电视台\\QTV.dpl')

#http://yingyong.aiqd.com.cn/api/v4/telecasts/channels/iqingdao?city_id=370200&uid=0&platform=2&nonce=123456&client_ver=5.0&device_id=9be5940516ad19bd1af87a81f04f32c2&client_id=370200&type=1&deviceId=9be5940516ad19bd1af87a81f04f32c2&timestamp=1516088787&signature=4fd1319af774e3b885d6c1642b7c2744f1bb36d497e48e63221de13bc4b94203&channel_id=782435920325386245

#http://yingyong.aiqd.com.cn/api/v4/telecasts/channels/iqingdao?uid=0&platform=2&client_ver=5.0.2&device_id=4438189f768ead5289109fb813c4b447&type=1&channel_id=782435920325386245&timestamp=1557733365&city_id=370200&nonce=123456&openid=0&client_id=370200&signature=7a2613f9aa98605c771a74eaf3e8e7fcdb30f6444f978489ac8e2a939bb47ffd&deviceId=4438189f768ead5289109fb813c4b447   QTV-1
#http://yingyong.aiqd.com.cn/api/v4/telecasts/channels/iqingdao?uid=0&platform=2&client_ver=5.0.2&device_id=4438189f768ead5289109fb813c4b447&type=1&channel_id=782435872518709253&timestamp=1557733416&city_id=370200&nonce=123456&openid=0&client_id=370200&signature=33487024adc151bec5184ea989974b5d5524c1767c71e5c091073ec447198fa7&deviceId=4438189f768ead5289109fb813c4b447   QTV-2
#http://yingyong.aiqd.com.cn/api/v4/telecasts/channels/iqingdao?uid=0&platform=2&client_ver=5.0.2&device_id=4438189f768ead5289109fb813c4b447&type=1&channel_id=782435817883705349&timestamp=1557733559&city_id=370200&nonce=123456&openid=0&client_id=370200&signature=73c77c8ac7f131c695ce51c12f4c8b40ee32096f335d51ab4bb38f31a949f7cf&deviceId=4438189f768ead5289109fb813c4b447   QTV-3
#http://yingyong.aiqd.com.cn/api/v4/telecasts/channels/iqingdao?uid=0&platform=2&client_ver=5.0.2&device_id=4438189f768ead5289109fb813c4b447&type=1&channel_id=782435770118971397&timestamp=1557733582&city_id=370200&nonce=123456&openid=0&client_id=370200&signature=15c0cd00d8a7fd6c16cf9a3a35c6fe7a246cc66f0f97b520d232f818b0ba7a6a&deviceId=4438189f768ead5289109fb813c4b447   QTV-4
#http://yingyong.aiqd.com.cn/api/v4/telecasts/channels/iqingdao?uid=0&platform=2&client_ver=5.0.2&device_id=4438189f768ead5289109fb813c4b447&type=1&channel_id=782435723360870405&timestamp=1557733621&city_id=370200&nonce=123456&openid=0&client_id=370200&signature=73f753a10b9e26a49498516e16cc36c48478ca414760259b796012e6f29e24fa&deviceId=4438189f768ead5289109fb813c4b447   QTV-5
#http://yingyong.aiqd.com.cn/api/v4/telecasts/channels/iqingdao?uid=0&platform=2&client_ver=5.0.2&device_id=4438189f768ead5289109fb813c4b447&type=1&channel_id=782435677038977029&timestamp=1557733647&city_id=370200&nonce=123456&openid=0&client_id=370200&signature=e8115b2de0f04553c1f5c82cd49c502aad6a2e8c21a2f367270a8d1df157cbfe&deviceId=4438189f768ead5289109fb813c4b447   QTV-6
#http://v2.91kds.cn/c9/sdqdtv.m3u8?id=sdqdtv3&app=org.jykds.tvlive&version=1.9.7&mac=ec:01:ee:17:ce:8a&nwtime=1557800601&sign=caefc5305bd12a889d8634fa8f9a083b&ev=20180910
#http://v2.91kds.cn/c9/sdqdtv.m3u8?id=sdqdtv4&app=org.jykds.tvlive&version=1.9.7&mac=ec:01:ee:17:ce:8a&nwtime=1557800685&sign=3612742e1753da34a3c752dcd3477706&ev=20180910
#http://v2.91kds.cn/c9/sdqdtv.m3u8?id=sdqdtv4&app=org.jykds.tvlive&version=1.9.7&mac=ec:01:ee:17:ce:8a&nwtime=1557800894&sign=abac90c01426c4e2c0b654135ecc175d&ev=20180910
#a712e8087705bdbdfd08c77a4ac9e7ae