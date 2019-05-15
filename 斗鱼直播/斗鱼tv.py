import requests
import os
import datetime
import time
from requests_toolbelt.multipart import MultipartEncoder
url='https://www.douyu.com/lapi/live/getH5Play/9999'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','referer':'https://www.douyu.com/60937','x-requested-with':'XMLHttpRequest','cookie': 'SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; dy_did=f558a0158e7b70198133928d00041501; acf_did=f558a0158e7b70198133928d00041501; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1556963168,1556971601,1557838409,1557923260; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1557923346','content-type':'application/x-www-form-urlencoded','origin':'https://www.douyu.com','content-type':'application/x-www-form-urlencoded'}
dir_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(dir_path,'test.txt')
t=int(time.time())
print(t)
files=open('C:\\Users\\Administrator\\PycharmProjects\\Channel\\战旗直播\\import.xls','a+')
m=MultipartEncoder({'file':('C:\\Users\\Administrator\\PycharmProjects\\Channel\\战旗直播\\import.xls',files),'v':'220120190515','did':'f558a0158e7b70198133928d00041501','tt':str(t),'sign':'1a104e36b21542f3f031fb9a7707f59c','rate':'4','ver':'Douyu_219050695','iar':'1','cdn':'ws-h5','iar':'0'})
#files={'v':('220120190515'),'did':('f558a0158e7b70198133928d00041501'),'tt':(str(t)),'sign':('1a104e36b21542f3f031fb9a7707f59c'),'rate':('4'),'ver':('Douyu_219050695'),'iar':('1'),'cdn':('ws-h5')}
r1= requests.post(url,data=m,headers=headers)
r = requests.post(url,data=m,headers=headers)
r.encoding = 'utf-8'
# r.encoding='GB2312'
r = r.text
print(r1)
print(r)