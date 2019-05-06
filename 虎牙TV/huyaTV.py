import requests
import string
import re
#huya={"测试电影":"11352903"}
huya={"周星驰电影":"11342412","林正英电影":"11342421","香港电影":"11352903","俗哥看电影":"15452736","四月好片":"880219","最新电影(成龙电影）":"11602087","豆瓣高分":"11602051","新三国":"11352944","周润发电影":"11342387","武林外传":"11601980","屌丝男士":"11342420","琅琊榜":"11352956","爱情公寓":"11336726","人民的名义":"11342425","MDL":"mdl2019","B神":"520888","longdd":"longdd","axx":"axx123","七龙珠改":'11601966','甄嬛传':'11601955','海绵宝宝':'11352919','猎场':'11342436','寻秦记':'11342417','战争电影':'11342435',"香港女神":"11336571","都市剧场":"11601979","宠物小精灵":"11336590",'apex1':'dada2','apex2':'kclo1z','apex3':'xinzhi','chiji1':'114421',"chiji2":'badaozongcai','chiji3':'lafeng','chiji4':'11526962','chiji5':'546540','zhuji1':'10428703','zhuji2':'vance','zhuji3':'13678069','zhuji4':'xiangge','恐怖游戏':'feima','恐怖游戏2':'125657','恐怖游戏3':'893974','xinyou1':'15635454','xinyou2':'zhilei','xinyou3':'guhe0','xinyou4':'16720240','xinyou5':'16457105','xinyou6':'16401363','xinyou7':'16484141','xinyou7':'18477904'}#,"":"","":""}
name=huya.keys()
ID=huya.values()
headers={"referer": "https://www.huya.com/l","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
yiqikan="http://www.huya.com/g/2135"
dota2="http://www.huya.com/g/dota2"
rx=requests.get(yiqikan,headers)
rx.encoding = 'utf-8'
txt2 = rx.text
rdota2=requests.get(dota2,headers)
rdota2.encoding = 'utf-8'
txtdota2 = rdota2.text
p1=r"https://www.huya.com/[1-9]{7,9}"
pattern1=re.compile(p1)
roomid=pattern1.findall(txt2)
roomdota2=pattern1.findall(txtdota2)
roomdota2id=list(set(roomdota2))
roomID = list(set(roomid))
roomdota2ID = list(set(roomdota2id))
for dota2rooms in roomdota2ID:
    dota2room=dota2rooms.replace("https://www.huya.com/","")
    #with open('dota2room.txt', 'a', encoding="utf-8") as f: f.write(dota2room+"\n")
for rooms in roomID:
    room=rooms.replace("https://www.huya.com/","")
    #with open('yiqikanroom.txt', 'a', encoding="utf-8") as f: f.write(room+"\n")
#with open('huyaTV.txt', 'w', encoding="utf-8") as f: f.write(txt2)
#i=txt2.find("https://www.huya.com/")
"""while i!=-1:
    i=txt2.find('<li class="game-live-item" gid="2135">')
    j=i+len('<li class="game-live-item" gid="2135">')
    m=j-i
    print(m)
    k=txt2.find('" class="',j)
    roomid=txt2[j:k]
    print(roomid)
    i=i+1
"""
for x in name:
    url="https://www.huya.com/"+huya[x]
    #headers={"referer": "https://www.huya.com/l","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
    r=requests.get(url,headers)
    r.encoding='utf-8'
    txt=r.text
    print(x,huya[x])
    #print(txt)
    n1=txt.find('"sHlsUrl":"')
    n2=txt.find('","',n1)
    #print(n1,n2)
    r1=txt[n1+len('"sHlsUrl":"'):n2]
    #print(r1)
    r2=r1.replace('\\','')
    #print(r2)
    n3=txt.find('"sStreamName":"')+len('"sStreamName":"')
    n4=txt.find('","sFlvUrl":"')
    r3=txt[n3:n4]
    #print(r3)
    playurl=r2+'/'+r3+'.m3u8'
    #with open('huyaTV.htm', 'w', encoding="utf-8") as f: f.write(txt)
    #with open('huyaTV.txt', 'w', encoding="utf-8") as f: f.write("")
    #with open('huyaTV.txt', 'w', encoding="utf-8") as f: f.write(playurl)
    #with open('huyaTV.txt', 'a', encoding="utf-8") as f: f.write(x+"\b"+huya[x]+"\b"+playurl+"\n")
    print(playurl)