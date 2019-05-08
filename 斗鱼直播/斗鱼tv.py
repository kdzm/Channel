import requests
import os
import datetime
import time
url='https://www.douyu.com/lapi/live/getH5Play/60937'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','referer':'https://www.douyu.com/60937','x-requested-with':'XMLHttpRequest','cookie': 'dy_did=b222fadcd86d2e4cd417bcd700021501; acf_did=b222fadcd86d2e4cd417bcd700021501; smidV2=20181127123132f45e0a53e29d0abe5ce6db6f2db2c33b000d1646772e36db0; _ga=GA1.2.1996915260.1543293204; acf_uid=2758026; acf_username=weibo_Phd2oCt6; acf_nickname=%E6%97%B6%E5%85%89%E6%A9%9F%E5%99%A8; acf_ltkid=80740881; acf_auth=7343s2I4XeY%2Fo8MnEn%2FhWrIoZBT8%2F5L3HnpYdaSOUxI2aFZlz6qaogrKHeP%2B5mQTiiyg7V1QmSAqHrMCfZH8nigKLmAvyMLPffONF%2FHNgkhmmQcxSkiQWmaHUps; wan_auth37wan=17b9e47c7e0aycVgSRcmnw3O9mmvVRhZ%2FCCUblvuNerZH7h0cf%2BT5xHTz826zqLGaiYz7WX1ct3l3R4WLOqhCPOKaksniLDPNk%2F08uihGkHMDwtr; acf_own_room=1; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_biz=1; acf_stk=ffdae7c987c0230e; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1557044044,1557278411; acf_avatar=//apic.douyucdn.cn/upload/avatar/002/75/80/26_avatar_; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; PHPSESSID=0rjij8vi3srv1cre22ct4tfef0; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1557278425'}
dir_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(dir_path,'test.txt')
t=time.time()
t=int(t)
print(t)
files={'v':('220120190508'),'did':('b222fadcd86d2e4cd417bcd700021501'),'tt':(str(t)),'sign':('2a99316dc299bfcad5ece9bd16daf488'),'rate':('4'),'ver':('Douyu_219050695'),'iar':('1'),'files':('test.txt',open(file_path,'rb'),'text/plain'),}
r = requests.post(url,files=files,headers=headers)
r.encoding = 'utf-8'
# r.encoding='GB2312'
r = r.text
print(r)