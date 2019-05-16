from requestget import geturl
import re
mgtv={'最新院线':'1258','悬疑动作':'1201','科幻大片':'3654','经典港片':'2991','动画电影':'2991','轻松喜剧':'1200','猪猪侠':'1089','喜洋洋':'1088','电视剧插曲':'1095','美女博主':'1230','勇敢的世界':'1234','花儿与少年':'1233','熊出没':'1243','超级飞侠':'1262','风再起时':'1256','樱桃小丸子':'1466','宝宝巴士':'1524','小猪佩奇':'1526','我是大侦探':'1546','江西舞蹈':'1576','寻情记':'1652','麻雀':'1215','日常护肤':'1230','中餐厅':'1812','a':'1869','芭比之梦境奇遇记':'1880','岳云鹏孙越':'1926','名侦探柯南':'1938','夏至未至':'2023','战地枪王':'2154','贝乐虎儿歌':'2274','骑上小绵羊':'2508','今日说法':'2555','熊鼠一家':'2603','妖神记第三季':'2683','军事观察':'2722'}#,'':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':''}#,'a':'','':''
headers={'User-Agent':'Dalvik/1.6.0 (Linux; U; Android 8.1.0; QABOX_1 Build/KOT49H)'}
us=[]
texts=[]
'''
file=open("C:\\Users\\Administrator\\PycharmProjects\\频道破解\\芒果TV\\mgid.txt","r+",encoding='utf-8')
f=file.read()
id=re.findall('新频道 - http://47.95.172.168/channel/(.+?)\.',f)
for i in id:
    url='http://ott.liveapi.mgtv.com/v1/epg/turnplay/getLivePlayUrlM3u8?platform=3&definition=??&ticket=&buss_id=1000014&device_id=098d061771538d551af94afdadb7e996&mac_id=BC-7F-E8-91-AD-51&uuid=mgtvmac&after_day=1&license===&net_id=&type=3&channel_id='+str(i)+'&version=5.5.115.200.2.DBEI.0.0_Release'
    r=geturl(url,headers=headers)
    if r.find('url')!=-1:
        print(i,url)'''
for x,y in mgtv.items():
    url='http://ott.liveapi.mgtv.com/v1/epg/turnplay/getLivePlayUrlM3u8?platform=3&definition=??&ticket=&buss_id=1000014&device_id=098d061771538d551af94afdadb7e996&mac_id=BC-7F-E8-91-AD-51&uuid=mgtvmac&after_day=1&license===&net_id=&type=3&channel_id='+y+'&version=5.5.115.200.2.DBEI.0.0_Release'
    r=geturl(url,headers=headers)
    u=re.findall('url":"(.+?)"',r)
    text=re.findall('text":"(.+?)"',r)
    texts=texts+text
    us=us+u
d=dict(zip(texts,us))
#print(d)
for z,x in d.items():
    y=x.encode('utf-8').decode('unicode_escape')
    us[us.index(x)]=y
    r2=geturl(us[us.index(y)],headers=headers)
    playurl=re.findall(r'info":"(.+?)"',r2)
    print(z,playurl)
#file.close()
# http://60.255.48.134:9090/live/chchd.m3u8
# http://60.255.48.134:9090/live/chcdzdy.m3u8
#http://60.255.48.134:9090/live/chcjtyy.m3u8
# http://asp.cntv.myalicdn.com/asp/hls/2000/0303000a/3/default/75bf10188ab14530a25b46fc031bfd22/2000.m3u8传奇大掌柜