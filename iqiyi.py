import requests
import os
import string
from DPL频道列表模板 import lists
iqiyi={"喜剧电影":"380168922","现代电视剧":"380115422","古装电视剧":"380176122","成龙电影":"380229022","倒霉熊":"380221722","爆笑虫子":"380221522","养生堂":"380216222","伪装者":"380216122","琅琊榜":"380215922","抗战剧场":"380215422","迪士尼":"380206722","如果爱":"380191822","陈奕迅":"380189122","奔跑吧兄弟":"380189222","樱桃小丸子":"380183622","军旅剧场":"380115122","XXX":"380102722","网球2":"380121722","奇葩说":"380228822","冯小刚":"380228922","兔小贝儿歌":"380222422","可可小爱":"380221622","谍战剧场":"380215722","郭德纲":"380207322","文化奇谈":"380207122","悠然小天":"380206822","动画电影":"380206422","爆笑精选":"380192122","爱情保卫战":"380191922","绝地求生":"380192022","亲子小游戏":"380191722","数码宝贝":"380189022","龙珠":"380188922","灌篮高手":"380188822","吃货":"380187022","美少女战士":"380185922","圣斗士星矢":"380186022","我的世界":"380186622","相亲选秀":"380115622","情感调节":"380115522","锦绣未央":"380115422","奇妙世界":"380121322","人文社会":"380116022","自然地理":"380115822","科学探索":"380115722","x":"380102722","武林风":"380121622","五星影院":"380173922","广场舞大全":"380186322","xx":"380102322","军事新闻":"380121222","亲子启蒙":"380185522","宝宝课堂":"380186522","":"380121122","c":"380078922","非常静距离":"380189522","热播综艺":"380189322","三生三世十里桃花":"380185322","动漫天地":"380188722","电影精选":"380187322","惊悚午夜剧":"380174022","好莱坞大片":"380173522","动作电影":"380173422","电影大片":"380187322","黑帮电影":"380173822","经典港片":"380173722","":"","":"","":"","":"","":"","":"","":"","":"","":""}
ID=iqiyi.values()
name=list(iqiyi.keys())
playurls=[]
for z in name:
    url="http://cache.video.ptqy.gitv.tv/liven/"+iqiyi[z]+"?lp=&src=04022001010000000000&pf=9&m=1583&qyid=tv_0291415626b010b5342b13bd743ee69b_1502353950858"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    r=requests.get(url,headers)
    r.encoding='utf-8'
    txt=r.text
    #print(x, iqiyi[x])
    #print(txt)
    n1=txt.rfind('"bitrate":"1200"')
    #print(n1)
    n2=txt.find("streamName",n1)
    #print(n2)
    url1 = txt[n1:n2]
    #print(url1)
    url2= url1.replace('"bitrate":"1200","url":"', "")
    url3=url2.replace('\\',"")
    playurl=url3.replace('","',"")
    if n1==-1:
        playurl='rtsp://125.88.53.18/PLTV/88888888/224/3221228112/10000100000000060000000007191279_0.smil'
    #print(playurl)
    playurls.append(playurl)
d=dict(zip(name,playurls))
#print(d)
    #with open('iqiyi.htm', 'a', encoding="utf-8") as f: f.write(x + ":" + playurl + "\n")
with open('iqiyi.htm', 'w', encoding="utf-8") as f: f.write(z + ":" + playurl + "\n")
with open('iqiyi.dpl', 'w', encoding="utf-8") as f: f.write('')
with open('iqiyi.dpl', 'w', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n' + 'playname=\n' + 'topindex=27\n' + 'saveplaypos=0\n')
for u in playurls:
    j=playurls.index(u)
    (x,y)=lists(name[j],u)
    with open('iqiyi.dpl', 'a+', encoding="utf-8") as f: f.write(str(j + 1) + x + "\n" + str(j + 1) + y + "\n" + str(j + 1) + '*played*0\n')
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\iqiyi.dpl')