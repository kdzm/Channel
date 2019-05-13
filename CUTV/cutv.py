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
id=re.findall(r'"id":"[0-9]{7}',r)
for x in id:
    n=id.index(x)
    n1[n]='http://cc.linkinme.com/nanning/'+x.replace('"id":"','')+"   "+n1[n].replace('\\','')
    print(n1[n])
#   rtmp://180.141.89.20/live/HXTV横县电视台     rtmp://180.141.89.20/live/MSTV马山电视台
