import requests
import string
import re
room={"芯芯CSGO":"288907"}
headers={"referer":"https://www.douyu.com/288907","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36","origin":"https://www.douyu.com","x-requested-with":"XMLHttpRequest","content-type":"application/x-www-form-urlencoded","accept":"application/json, text/plain, */*","cookie":"dy_did=b222fadcd86d2e4cd417bcd700021501; acf_did=b222fadcd86d2e4cd417bcd700021501; smidV2=20181127123132f45e0a53e29d0abe5ce6db6f2db2c33b000d1646772e36db0; _ga=GA1.2.1996915260.1543293204; acf_uid=2758026; acf_username=weibo_Phd2oCt6; acf_nickname=%E6%97%B6%E5%85%89%E6%A9%9F%E5%99%A8; acf_ltkid=80740881; PHPSESSID=nqsn96v4l2pdlplubaj7uuaih1; acf_auth=fccbGq2n0OUVyBFrp52%2FCbGQtlUKMgDfRGBJ3kGStLVFpJdCVegaSWxjhwasEN2%2FE5l5b3Ue8wAF21pD%2BpmxLE7clqNW%2BK5HcEXch3FKgd0TMaePJgmRomFpLBw; wan_auth37wan=210ca8045433Zx3uoee9gvo8zNoLkbRh26RituLPwXJ817WNecc2ukEFTJUU1JVSwRTJw0qskrN9S9AZTS3%2Bt9gYeSWq13WoPgjPdkYFeC271HCW; acf_own_room=1; acf_groupid=1; acf_phonestatus=1; acf_avatar=https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar%2F002%2F75%2F80%2F26_avatar_; acf_ct=0; acf_biz=1; acf_stk=d7f2454b292874ec; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1552982272,1552986231,1553162958,1554178104; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1554187265"}
#url="https://www.douyu.com/lapi/live/getH5Play/288907"
name=room.keys()
data={"v": "220120190402","did":"b222fadcd86d2e4cd417bcd700021501","tt": "1554188453","sign":"d1f58d5869d91399c8ff0809e8d51777","cdn": "","rate:":" 0","ver":"Douyu_219040295","iar":"1","ive": "0"}
for x in  name:
    url = "http://www.douyu.com/lapi/live/getH5Play/"+room[x]
    r=requests.post(url,data,headers=headers)
    r.encoding = 'utf-8'
    txt1= r.text
    print(txt1)