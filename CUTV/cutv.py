#南宁
from requestget import geturl
import re
urlnn='http://app.nntv.cn/api/tt_live.php?type=1' \
      'http://app.nntv.cn/api/tt_live.php?type=1'
header1={'User-Agent': 'LuaSocket 3.0-rc1'}
r=geturl(urlnn,headers=header1)
print(r)
n1=re.findall(r'http:\\/\\/m3u8.nntv.cn.+?.m3u8',r)
#n2=r.find('sd.m3u8',n1)+len('sd.m3u8')
#video_url=r[n1:n2].replace('\\','')
n1.remove(n1[1])
n1.remove(n1[5])
n1.remove(n1[5])
n1.remove(n1[5])
n1.remove(n1[6])
n1.remove(n1[9])
id=re.findall(r'"id":"[0-9]{7}',r)
id.remove((id[1]))
id.remove(id[5])
id.remove(id[5])
id.remove(id[5])
id.remove(id[6])
id.remove(id[9])
name=['南宁新闻综合','南宁都市频道','南宁影视娱乐','南宁公共频道','cctv13','MSTV','横县电视台','马山电视台','CCTV1']
for x in id:
    n=id.index(x)
    name[n]=name[n]+"   "+x.replace('"id":"','')
dl=dict(zip(name,n1))
for i in n1:
    print(i.replace('\\',''))
for x,y in dl.items():
    y=y.replace('\\','')
    print(x,y)