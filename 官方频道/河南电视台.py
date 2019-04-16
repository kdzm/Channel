import string
from requestget import geturl
dlist={'都市频道':'136'}
name=dlist.keys()
for i in name:
    url="http://www.hntv.tv/soms4/servlet/FlashInterfaceServlet?function=GetLiveProgramInfo&channelId="+dlist[i]
    headers={"Referer":"http://www.hntv.tv/soms4/web/jwzt/player/flashplayer/program_live_player_flash.jsp?function=GetLiveProgramInfo&channelId="+dlist[i],
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3760.0 Safari/537.36 Edg/75.0.125.0"}
    r=geturl(url,headers=headers)
    print(r)
'''
136都市频道
137民生频道
138法制频道
139电视剧频道
140新闻频道
141欢腾购物
142公共频道
143新农村频道
144国际频道
145晴彩中原
146移动戏曲
147武术世界
148梨园频道
149文物宝库
152文新春茶节
'''