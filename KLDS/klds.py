
from requestget import geturl
headers={'User-Agent': 'okhttp/3.9.1','Host': 'apiklds.clouddianshi.com:8882','SAAS': 'cn.grtech.tv'}
url='http://apis.abc.com/ntvlive/newstest'
url2='http://live.stream.tvmcloud.com/token/uatoken?app=js&format=json&string=eJwdyMsKwjAQBdAvEibTzvRmJ65c1seiu5BJjCCVahHaQj5ecXc4yxqmZTf0j%2FEyy7kf%2FR2363T4DE%2BZw%2FEUaK%2FEMHDHJVlmB%2FOa1dmvyl%2F1Dd5eUmuhNiFHKhHWEmCpc9wIRVKv0vAXNXQgLQ%3D%3D'
r=geturl(url,headers=headers)
print(r)