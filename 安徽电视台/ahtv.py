import requests
lists={'经济生活':'jjsh','综艺频道':'zypd','安徽影视':'yspd','安徽人物':'rwpd','安徽科教':'kjpd','安徽国际':'ahgj','安徽公共':'ahgg','安徽卫视':'ahws'}
headers2={'User-Agent':'ExoPlayer/9.9.9 (Linux;Android 4.4.4) ExoPlayerLib/2.5.1','Referer':'http://v.ahtv.cn/'}
for x,y in lists.items():
    url='http://v.ahtv.cn/m2o/m3u8.php?url=http://live.ahtv.cn/live/'+y+'.m3u8'
    res = requests.get(url, allow_redirects=False)
    la = res.headers['location']
    print(x,la)
'''
http://v.ahtv.cn/m2o/m3u8.php?url=http://live.ahtv.cn/live/jjsh.m3u8    经济生活
http://v.ahtv.cn/m2o/m3u8.php?url=http://live.ahtv.cn/live/zypd.m3u8    综艺频道
http://v.ahtv.cn/m2o/m3u8.php?url=http://live.ahtv.cn/live/yspd.m3u8    安徽影视
http://v.ahtv.cn/m2o/m3u8.php?url=http://live.ahtv.cn/live/rwpd.m3u8    安徽人物
http://v.ahtv.cn/m2o/m3u8.php?url=http://live.ahtv.cn/live/kjpd.m3u8    安徽科教
http://v.ahtv.cn/m2o/m3u8.php?url=http://live.ahtv.cn/live/ahgj.m3u8    安徽国际
http://v.ahtv.cn/m2o/m3u8.php?url=http://live.ahtv.cn/live/ahgg.m3u8    安徽公共
http://v.ahtv.cn/m2o/m3u8.php?url=http://live.ahtv.cn/live/ahws.m3u8    安徽卫视
'''