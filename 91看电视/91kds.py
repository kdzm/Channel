import time
from requestget import geturl
import random
import requests
import re
import os
import string
'''
t0=time.perf_counter()
t1 = time.perf_counter()
print(t1)'''
headers={'Referer':'http://m.91kds.org/jiemu_sdqdtv1.html','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
def get_livekey():
    auth = 'http://m.91kds.org/auth3.php?t=' + str(random.random())
    r = geturl(auth,headers=headers)
    livekey=re.findall(r'(nwtime.+?)"',r)
    livekey=livekey[0]
    return livekey
print(get_livekey())
file=open("C:\\Users\\Administrator\\PycharmProjects\\频道破解\\91看电视\\91ktv.txt","r+",encoding='utf-8')
#得到livekey
f=file.read()
auth='http://m.91kds.org/auth3.php?t='+str(random.random())
r=geturl(auth,headers=headers)
print(r)
n1=r.find('":"')+len('":"')
n2=r.find('"',n1)
livekey=r[n1:n2]

#创建青岛电视台函数
def qtv(a,b):
    qtv_url='http://v.91kds.cn/c9/'+a+'.m3u8?id='+b+'&'+livekey
    print(qtv_url)
    headers2 = {'Referer': 'http://m.91kds.org/jiemu_cctv1.html',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
                'Accept-Encoding': 'identity;q=1, *;q=0', 'chrome-proxy': 'frfr', }
    r=geturl(qtv_url,headers=headers2)
    print(b+'\n',r)
qtv_lists=['sdqdtv1','sdqdtv2','sdqdtv3','sdqdtv4','sdqdtv5','sdqdtv6']
for x in qtv_lists:
    a=qtv('sdqdtv',x)

#央视频道
cctv1='http://v.91kds.cn/b9/shydmg.m3u8?id=cctv1hd&'+livekey
res=requests.get(cctv1,headers=headers,allow_redirects=False)
#print(res)
la = res.headers['location']
print(la)

#爱艺奇轮播台，http://v.91kds.cn/b9/qiyi2.m3u8?id=qiyicl&nwtime=1557818476&sign=d9a46637b29a4c56e8f42fe3110a1191&mip=61.144.147.38&from=com
def qiyi2(a,b):
    qiyi='http://v.91kds.cn/b9/'+a+'.m3u8?id='+b+'&'+livekey
    r=requests.get(qiyi,headers=headers,allow_redirects=False)
    la=r.headers['location']
    #print(b,la)
    return la
qiyiid=['qiyicl','qiyilz','qiyiqh','qiyixq','qiyiatm','qiyidmx','qiyifxg','qiyihqg','qiyihsy','qiyilyb','qiyitkx','qiyiwzz','qiyixyy','qiyixzq','qiyiyst','qiyiyyp','qiyizjl','qiyizrx','qiyiaqgy','qiyibbbs','qiyibbkt','qiyibweg','qiyibxcz','qiyibxjx','qiyidhdy','qiyidjcw','qiyidlam','qiyidmly','qiyidtez','qiyidwxd','qiyidydp','qiyidzdy','qiyidzjc','qiyifcwr','qiyiglgs','qiyihbdy','qiyihjdh','qiyijdgp','qiyijdjc','qiyijljc','qiyijsgc','qiyijtjc','qiyijyen','qiyikjys','qiyikkxa','qiyikxjc','qiyikxts','qiyikzjc','qiyilbxx','qiyilsmw','qiyilygl','qiyimhls','qiyimscf','qiyindjc','qiyiobjc','qiyiqbeg','qiyiqgtj','qiyiqmsj','qiyiqzqm','qiyirwsh','qiyirxbj','qiyismbb','qiyisqbb','qiyissss','qiyitqbk','qiyiwdsj','qiyiwhqt','qiyiwjly','qiyiwlwz','qiyiwqss','qiyiwxyy','qiyixjdk','qiyixjdy','qiyixqxx','qiyixsxp','qiyiyrxt','qiyiyweg','qiyiyxlm','qiyizbzy','qiyizrdl','qiyiaqbwz','qiyibpbxd','qiyidhxtd','qiyigcwdq','qiyihlwdp','qiyijswyc','qiyimsnzs','qiyimxfsh','qiyiqzxyx','qiyirbdsj','qiyirmdmy','qiyisdsxs','qiyitxbeg','qiyiwpdwp','qiyibllxmx']
#qiyiurl=[]
'''
qyname=re.findall(r'"name": "(爱奇艺.+?)"',f)
qyid=re.findall(r'ename": "(qiyi.+?)"',f)
#print(len(qyname))
#print(len(qyid))
qyd=dict(zip(qyname,qyid))
del qyd['爱奇艺高尔夫球']
with open('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\爱奇艺\\iqiyi.txt', 'w', encoding="utf-8") as f: f.write('')
for y,x in qyd.items():
    qy1=qiyi2('qiyi2',x)
    n=qy1.find('m3u8')+4
    qy1=qy1[0:n]
    qy1=qy1.replace('hlslive.video.ptqy.gitv.tv','113.113.73.41/r/baiducdnct.inter.iqiyi.com')
    #qiyiurl.append(qy1)
    print(y,qy1)
    with open('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\爱奇艺\\iqiyi.txt', 'a+', encoding="utf-8") as f: f.write(y+','+qy1+'\n')
#print(len(qiyiurl))
'''


#http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp  得到时间戳
#CIBN轮播台
'''
CIBN嗨播,http://gs.hdp.ds.lunbocl.ott.CIBNtv.net/hls/vCIBNDYDYYPD/1800/vCIBNYYPD.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN古装剧场,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNZYPD/1800/vCIBNZYPD.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN汉学院,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNHXYPD/1800/vCIBNHXYPD.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN记录片,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNJLPD/1800/vCIBNJLPD.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN汽车,http://gs.hdp.ds.lunbocl.ott.CIBNtv.net/hls/vCIBNQCPD/1800/vCIBNQCPD.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN情感影院,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNQGYY/1800/vCIBNQGYY.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN军事,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNGZJC/1800/vCIBNGZJC.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN教育,http://gs.hdp.ds.lunbocl.ott.CIBNtv.net/hls/vCIBNJYPD/1800/vCIBNJYPD.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN骄阳剧场,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNJDJC/1800/vCIBNJDJC.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN生活,http://gs.hdp.ds.lunbocl.ott.CIBNtv.net/hls/vCIBNGWPD/1800/vCIBNGWPD.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN炫佳动漫,http://gs.hdp.ds.lunbocl.ott.CIBNtv.net/hls/vCIBNDMPD/1800/vCIBNDMPD.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN童学世界,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNRBJC/1800/vCIBNRBJC.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN文化中国,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNCWHPD/1800/vCIBNCWHPD.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN微电影,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNWDYPD/1800/vCIBNWDYPD.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN电影导视,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNDYDS/1800/vCIBNDYDS.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN喜剧影院,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNHSYX/1800/vCIBNHSYX.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN电影,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNDYPD/1800/vCIBNDYPD.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN好莱坞,http://mgzb.live.miguvideo.com:8088/wd_r3/peoplecn/cibnhaolaiwu/350/01.m3u8?msisdn=migu&mdspid=&spid=699011&netType=0&sid=5500094581&pid=2028597139&timestamp=20190514171049&Channel_ID=1004_10010001005&ProgramID=621634965&ParentNodeID=-99&assertID=5500094581&client_ip=117.153.83.145&SecurityKey=20190514171049&promotionId=&mvid=&mcid=&mpid=&mtv_session=480ea336436a181d8a34a37345685453&HlsSubType=1&HlsProfileId=1&nphaid=0&encrypt=ae2c43319efa427b539b9cfbab4ea7e9
CIBN院线大片,http://mgzb.live.miguvideo.com:8088/wd_r4/peoplecn/yuanxiandapian/350/01.m3u8?msisdn=migu&mdspid=&spid=699011&netType=0&sid=5500205106&pid=2028597139&timestamp=20190514171209&Channel_ID=1004_10010001005&ProgramID=624185089&ParentNodeID=-99&assertID=5500205106&client_ip=117.153.83.145&SecurityKey=20190514171209&promotionId=&mvid=&mcid=&mpid=&mtv_session=e2316acc1d3d083d6028460109314f57&HlsSubType=1&HlsProfileId=1&nphaid=0&encrypt=2213562c3ffebe3cce86279b20e129c1
CIBN财经,http://mgzb.live.miguvideo.com:8088/wd_r4/peoplecn/cibncaijing/350/01.m3u8?msisdn=migu&mdspid=&spid=699011&netType=0&sid=5500136824&pid=2028597139&timestamp=20190514171537&Channel_ID=1004_10010001005&ProgramID=622324891&ParentNodeID=-99&assertID=5500136824&client_ip=117.153.83.145&SecurityKey=20190514171537&promotionId=&mvid=&mcid=&mpid=&mtv_session=7ffa938718419d83d5194c74b2f441f0&HlsSubType=1&HlsProfileId=1&nphaid=0&encrypt=98a2def3450040d0ff4a1694cee48166
CIBNTEA电竞,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNTEADJ/1800/vCIBNTEADJ.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN钓鱼,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNHWXF/1800/vCIBNHWXF.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
CIBN精品影院,http://gs.hdp.ds.lunbocl.ott.cibntv.net/hls/vCIBNJPYY/1800/vCIBNJPYY.m3u8?md5=c246ac4e6b6cb88b7f970b530ff04b86
'''
cibn_name=re.findall(r'"name": "(CIBN.*?)"',f)
cibn_id=re.findall(r'"ename": "(cibn.*?)"',f)
cibns=dict(zip(cibn_name,cibn_id))
del cibns['CIBN钓鱼']
def cibn(b):
    cibnurl='http://v.91kds.cn/b9/rmsx.m3u8?id='+b+'&'+livekey
    #print(cibnurl)
    ra=requests.get(cibnurl,headers=headers,allow_redirects=False)
    #print(ra)
    l=ra.headers['location']
    return l
for x,y in cibns.items():
    playurl=cibn(y)
    print(x,playurl)

#91kds 安徽
'''
http://124.232.231.246:6610/000000001001/201500000142/index.m3u8?IASHttpSessionId=OTT   安徽人数
http://61.58.60.230:9319/live/237.m3u8  安徽国际
http://youyoulive02.anhuibvc.com/youyoutv/stream13.m3u8?auth_key=1611225641-0-0-3708746de1e4851289165ba5a61fff6a    安徽导视
http://111.40.205.87/PLTV/88888888/224/3221225745/index.m3u8    哈尔滨新闻   http://39.135.135.65/PLTV/88888888/224/3221225684/index.m3u8?icpid=88888888&from=1&hms_devid=175,680
http://111.40.205.87/PLTV/88888888/224/3221225760/index.m3u8哈尔滨影视http://39.134.65.162/PLTV/88888888/224/3221225700/index.m3u8
http://111.40.205.87/PLTV/88888888/224/3221225761/index.m3u8哈尔滨资讯http://39.134.65.162/PLTV/88888888/224/3221225697/index.m3u8
http://111.40.205.87/PLTV/88888888/224/3221225762/index.m3u8哈尔滨生活http://39.134.65.162/PLTV/88888888/224/3221225698/index.m3u8
http://111.40.205.87/PLTV/88888888/224/3221225759/index.m3u8哈尔滨娱乐http://39.134.65.162/PLTV/88888888/224/3221225699/index.m3u8
'''
#广州
#深圳电视台
#广西南宁
nnlist={"南宁新闻综合":"gxnntv1","南宁影视娱乐":"gxnntv2","南宁都市生活":"gxnntv3","南宁公共频道":"gxnntv4"}
def gxnn(n,b):
    nnurl='http://v.91kds.cn/b9/'+n+'.m3u8?id='+b+'&'+livekey
    rn=requests.get(nnurl,headers=headers,allow_redirects=False)
    ln=rn.headers['location']
    return ln
for x,y in nnlist.items():
    pl=gxnn('sdqk1',y)
    print(x,pl)

def get_location(n,b):
    url=nnurl='http://v.91kds.cn/b9/'+n+'.m3u8?id='+b+'&'+livekey
    r=requests.get(url,headers=headers,allow_redirects=False)
    la=r.headers['location']
    return la

#海南卫视
#河南电视台
#江苏

#广州
gdgztv_list=['gdgzzh','gdgzxw','gdgzys','gdgzsh','gdgzjj','gdgzse','gdgzjs']
for x in gdgztv_list:
    print(get_location('gdgztv',x))
print('\n')
#深圳
gdsztv_list=['gdszds','gdszdsj','gdszyl','gdszty','gdszse','gdszgg','gdszdv','gdszgj','gdszba','gdszdb','gdszyd']
for x in gdsztv_list:
    print(get_location('gdsztv',x))
#http://ts10.sztv.com.cn/15e2c816f6a74eac8403c295212a0936/h264_500k_ts/index.m3u8?type=flv2hls_m3u8深圳财经
#http://183.207.248.71/cntv/live1/shenzhenstv/shenzhenstv深圳卫视

#cutv
#cutv=re.findall(r'')

file.close()

