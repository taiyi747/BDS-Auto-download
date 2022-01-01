import requests
import os
from bs4 import BeautifulSoup
file="/root/bdsfile"
bdslog=file+"/BDSlog"
if os.path.exists(bdslog):
    print("检测BDSlog文件存在")
else:
    print("检测到BDSlog文件不存在,创建bdslog文件")
    f=open(file+"/BDSlog","w+",encoding='utf8')
    f.close()
#处理记录
f=open(bdslog,"r+",encoding='utf8')
bds=[]
for i in f.readlines():
    bds.append(i.strip())
#请求结果
r=requests.get('https://ssk.taiyu.workers.dev/zh-hans/download/server/bedrock')
soup = BeautifulSoup(r.text,'lxml')
print("请求结果："+str(r.status_code))
url=soup.find("a",attrs={"class" :"btn btn-disabled-outline mt-4 downloadlink"}).get("href")
filename=url.split("/")[-1]
print("BDS最新版本："+filename)
if filename in bds:
    print("文件已存在")
else:
    print("开始下载")
    linux=os.system("wget "+"-q -P "+file+"/linux "+"https://minecraft.azureedge.net/bin-linux/"+filename)
    win=os.system("wget "+"-q -P "+file+"/win "+"https://minecraft.azureedge.net/bin-win/"+filename)
    bds.append(filename)
    print("下载完成")
for i in bds:
    f.write(str(i)+"\n")
    f.close
