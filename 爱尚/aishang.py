from requestget import geturl
import uuid
chlist={'cctv1':'00000110240127_1','cctv3':'00000110240245_1','cctv4':'00000110240316_1','cctv5':'00000110240246_1',"cctv7":'00000110240248_1','cctv8':'00000110240249_1',"cctv9":'00000110240250_1','cctv10':'00000110240251_1','cctv12':'00000110240252_1'}
for x in chlist.keys():
    u=uuid.uuid4()
    url='http://47.95.69.248/gslb/live?stream_id='+x+'&region=310000&isp=telecom&uuid='+str(u)+'&ver=1.0.8'
    headers={'User-Agent': 'ExoPlayer/9.9.9 (Linux;Android 4.4.4) ExoPlayerLib/2.5.1'}
    r=geturl(url,headers=headers)
    #print(r)
    if r.find('"avc,mp21"')!=-1:
        n1=r.find('/0/')+3
        n2=r.find('\n#EXTM3U')
        ur=r[n1:n2]
    elif r=='':
        ur=''
    else:
        n1=r.find('/0/')+3
        ur=r[n1:-1]
    #print(n1)
    if r=='':
        playurl=''
    else:
        playurl='http://live.aishang.ctlcdn.com/'+chlist[x]+'/'+ur
    print(x,playurl)

#http://live.aishang.ctlcdn.com/00000110240127_1/playlist.m3u8?CONTENTID=00000110240127_1&AUTHINFO=FABqh274XDn8fkurD5614gM2WskyVx2lTv2Q2v%2B%2FB0%2BA1dCWrX8Ya72zEnc7Vc30XaSdwYK%2BdePzag2MGUw%2FdE8ZRItRJMEe3Qlo0xingHerdFb4EhE%2ByR%2BZ9afgYmcQZ5Ti53Jkdog%2BQEIiSMiQqnSM9D%2FTuZbrVNcqM1nFFl7SK7R35nSfKdaQR5NmR9iGBZuqBYSnToEkYeB2tQYfrw%3D%3D&USERTOKEN=7HT0UxWHLD67z1i4zpgoeOB0O2BhR0KR