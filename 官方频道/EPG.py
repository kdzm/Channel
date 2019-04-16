from requestget import geturl
import string
import re
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3757.0 Safari/537.36 Edg/75.0.124.0","cookies":"BAIDU_SSP_lcr=http://121.42.137.110:8080/szbox/admin/live/live-channel!list.htm; loc=440100; UM_distinctid=16a064e6159762-0635f9d12db2d6-2f5a044a-1fa400-16a064e615a7b2; _ga=GA1.2.664876105.1554883961; _gid=GA1.2.308974554.1554883962; Hm_lvt_a27d3c53126c59f93b8f63a30262cb5e=1554883961,1554883966; JSESSIONID=F50A456FB5B801512FCB21FF2A4937D7; Hm_lpvt_a27d3c53126c59f93b8f63a30262cb5e=1554891871; CNZZDATA1255238971=1832186888-1554880990-null%7C1554891274; tmid=18444419_61.144.145.47; FAD=1"}
url='https://www.tvsou.com/epg/CCTV-2?class=yangshi'
r=geturl(url,headers=headers)
#print(r)
time=r"<span>[0-9]{2}:[0-9]{2}</span>"
pattern1=re.compile(time)
name=r'"_blank">.+?</a>'
pattern2=re.compile(name)
times1=pattern1.findall(r)
names1=pattern2.findall(r)
times=[]
names=[]
names1.pop()
for x in times1:
    x=x.replace("<span>","").replace("</span>","")
    times.append(x)
for y in names1:
    y=y.replace('"_blank">','').replace('</a>','')
    names.append(y)
epg=dict(zip(times,names))
for x in epg.items():
    print(x)
'''  
print(len(times))
print(len(names1))
for t in times:
    #print(times)
    n=times.index(t)
    print(t,names1[n])
print("\n")
names1.pop()
for i in names1:
    print(names1.index(i),i)
'''
#https://www.tvmao.com/api/pg?p=JhBRkQ2MEE5RUM0QjcwOEUwNjg5QUFBRjAzMUE%3DOUQxMTAyN0E2ODRGMDNGRTI4MDAxMzNFNTZEOUY4OTVFNTk5MDI4MzA2fENDNEMwQjc3MUNFNjY5NjNGQzE4MkNEMkI0MkI1NzY1MUU%3DfDg5MjZCMjNCNTFDNTk1OUJBNkIwQTI4MTgwOEVBQT
#https://www.tvmao.com/api/pg?p=JQTBCMjJEMUUwOEI4NjhENjcwRDg2QTk3RjFGRkI3RDRFQ0M2RjM3Q0Q3fEJEMkM4MDQyNjlDQ0FBM0YxOEU4NTY1OUMxMTUwQTgyQkU%3DfDYzODM4OUE0REIzRDA4MkUzNTAxNzFGMjEyN0NDNDk2ODFFMjJBNkFGMEFCMDY1NDFFNjI4N0FBMkY%3D