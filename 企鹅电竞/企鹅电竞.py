from requestget import geturl
from requestget import posturl
import requests
from DPL频道列表模板 import lists
import re
import os
file=open("C:\\Users\\Administrator\\PycharmProjects\\频道破解\\企鹅电竞\\一起看搜集.txt","r+",encoding='utf-8')
f=file.read()
qq='https://egame.qq.com/gamelist'
headers={'referer':'https://egame.qq.com/gamelist/1','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','cookie':'pgv_pvi=9228730368; RK=r/S1yN41FW; ptcz=39b8c9638510908e7a35e3b4165e9f21dd7046db334b26a3348992043178e0c9; pgv_pvid=2950126576; tvfe_boss_uuid=d5395c453ab400ae; o_cookie=1322093265; pac_uid=1_1322093265; pgg_pvid=184977408019050810; new_device=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216a958239e43b7-043da707ff527c-6353160-2073600-16a958239e54c4%22%2C%22%24device_id%22%3A%2216a958239e43b7-043da707ff527c-6353160-2073600-16a958239e54c4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; pgv_si=s1035228160; uin=o1322093265; skey=@MIkiAqUvt; ptisp=ctc; pgg_ssid=14551961619051609; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1'}
#class1={'一起看':'2000000110','主机游戏':'2000000140'}
class1={'一起看':'2000000110'}

def QQliveClass():
    r=geturl(qq,headers=headers)
    #print(r)
    layoutid=re.findall(r'a href="/livelist\?layoutid=(.+?)"',r)
    titles=re.findall(r'target="_blank" title="(.+?)"',r)
    del titles[0]
    d=dict(zip(titles,layoutid))
    #for x,y in d.items():
        #print(x,y)
    return d
    #print(r)
m=QQliveClass()
#print(m)
print('----------------------')
m1={'一起看':'2000000110'}
#m1={'一起看':'2000000110','王者荣耀':'1104466820','和平精英': '1106467070','英雄联盟': 'lol'}
for i,j in m1.items():
    playurls = []
    #print(i)
    #with open('企鹅电竞.txt', 'w', encoding="utf-8") as f:f.write('i\n')
    #urls='https://egame.qq.com/livelist?layoutid='+j
    '''
    for n in range(1,5):

        url='https://share.egame.qq.com/cgi-bin/pgg_live_async_fcgi?param=%7B%22key%22:%7B%22module%22:%22pgg_live_read_ifc_mt_svr%22,%22method%22:%22get_pc_live_list%22,%22param%22:%7B%22appid%22:%222000000110%22,%22page_num%22:'+str(n)+'%22page_size%22:40,%22tag_id%22:0,%22tag_id_str%22:%22%22%7D%7D%7D&app_info=%7B%22platform%22:4,%22terminal_type%22:2,%22egame_id%22:%22egame_official%22,%22imei%22:%22%22,%22version_code%22:%229.9.9.9%22,%22version_name%22:%229.9.9.9%22%7D&g_tk=1189253248&p_tk=&tt=1&_t=1557970472533'
        r=geturl(url,headers=headers)
        print(r)
        '''
    room_id=re.findall(r'"anchor_id":(\d*),',f)
    room_name=re.findall(r'anchor_name":"(.+?)"',f)
    print(len(room_id))
    print(len(room_name))
    #if n==1:
       # del room_name[0]
    class_allroom=dict(zip(room_name,room_id))
    #del class_allroom['下载APP']
    for x,y in class_allroom.items():
        room_url='https://egame.qq.com/'+y
        res=geturl(room_url,headers=headers)
        playurl=re.findall(r'playUrl":"(.+?.flv)',res)
        if len(playurl)==0:
           playurl='http://3954.liveplay.myqcloud.com/live/3954_320942587.flv'
        else:
            playurl=playurl[0]
        playurls.append(playurl)
        print(x+'\t',playurl)
    print('----------------------')
    with open(i+'.dpl', 'w', encoding="utf-8") as f: f.write('')
    with open(i+'.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0\n')
    for u in playurls:
        j=playurls.index(u)
        (x,y)=lists(room_name[j], u)
        with open(i+'.dpl', 'a+', encoding="utf-8") as f: f.write(str(j + 1) + x + "\n" + str(j + 1) + y + "\n" + str(j + 1) + '*played*0\n')
    os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
    os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\企鹅电竞\\'+i+'.dpl')
file.close()