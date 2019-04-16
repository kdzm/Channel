import requests
from requestget import geturl
list={'cctv1':"119"}
name=list.values()
for x in name:
    url='http://live.xocs.ren/nx.php?id='+list[x]
    r=geturl(url)
    print(r)