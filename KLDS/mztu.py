import requests
from lxml import etree
sr=[]
at=[]
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',"referer":"https://www.mzitu.com/tag/ugirls"}
for x in range(1,17):
    if x==1:
        url='https://www.mzitu.com/tag/ugirls'
    else:
        url='https://www.mzitu.com/tag/ugirls/page/'+str(x)+'/'
    r=requests.get(url)
    html=etree.HTML(r.text)
    src_list=html.xpath('//img[@class="lazy"]/@data-original')
    alt_list=html.xpath('//img[@class="lazy"]/@alt')
    for a in src_list:
        at.append(a)
    for b in alt_list:
        sr.append(b)
for alt,src in zip(sr,at):
    #print(alt,src)
    response=requests.get(src,headers=headers)
    file_name="iphone\\"+alt+".jpg"
    #print("正在保存文件:",file_name)
    with open(file_name,"wb") as f:f.write(response.content)
