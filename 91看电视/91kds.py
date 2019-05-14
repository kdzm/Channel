import time
from requestget import geturl
import random
import requests
import string
'''
t0=time.perf_counter()
t1 = time.perf_counter()
print(t1)'''

#得到livekey
auth='http://m.91kds.org/auth3.php?t='+str(random.random())
print(auth)
headers={'Referer':'http://m.91kds.org/jiemu_sdqdtv1.html','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
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
    print(b,la)
qiyiid=['qiyicl','qiyilz','qiyiqh','qiyixq','qiyiatm','qiyidmx','qiyifxg','qiyihqg','qiyihsy','qiyilyb','qiyitkx','qiyiwzz','qiyixyy','qiyixzq','qiyiyst','qiyiyyp','qiyizjl','qiyizrx','qiyiaqgy','qiyibbbs','qiyibbkt','qiyibweg','qiyibxcz','qiyibxjx','qiyidhdy','qiyidjcw','qiyidlam','qiyidmly','qiyidtez','qiyidwxd','qiyidydp','qiyidzdy','qiyidzjc','qiyifcwr','qiyiglgs','qiyihbdy','qiyihjdh','qiyijdgp','qiyijdjc','qiyijljc','qiyijsgc','qiyijtjc','qiyijyen','qiyikjys','qiyikkxa','qiyikxjc','qiyikxts','qiyikzjc','qiyilbxx','qiyilsmw','qiyilygl','qiyimhls','qiyimscf','qiyindjc','qiyiobjc','qiyiqbeg','qiyiqgtj','qiyiqmsj','qiyiqzqm','qiyirwsh','qiyirxbj','qiyismbb','qiyisqbb','qiyissss','qiyitqbk','qiyiwdsj','qiyiwhqt','qiyiwjly','qiyiwlwz','qiyiwqss','qiyiwxyy','qiyixjdk','qiyixjdy','qiyixqxx','qiyixsxp','qiyiyrxt','qiyiyweg','qiyiyxlm','qiyizbzy','qiyizrdl','qiyiaqbwz','qiyibpbxd','qiyidhxtd','qiyigcwdq','qiyihlwdp','qiyijswyc','qiyimsnzs','qiyimxfsh','qiyiqzxyx','qiyirbdsj','qiyirmdmy','qiyisdsxs','qiyitxbeg','qiyiwpdwp','qiyibllxmx']
'''
for x in qiyiid:
    qy1=qiyi2('qiyi2',x)'''

#http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp  得到时间戳
#CIBN轮播台
def cibn(a,b):
    cibnurl='http://v.91kds.cn/b9/'+a+'.m3u8?id='+b+'&'+livekey
    print(cibnurl)
    ra=requests.get(cibnurl,headers=headers,allow_redirects=False)
    print(ra)
    l=ra.headers['location']
    print(b,l)
cibn1=cibn('rmsx','cibndm')
#91kds 安徽
#广州
#深圳电视台
#广西南宁
#海南卫视
#河南电视台
#江苏

