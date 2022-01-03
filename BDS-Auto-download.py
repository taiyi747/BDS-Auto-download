import requests
import os
from bs4 import BeautifulSoup
##————————————配置文件，自行修改——————————————##
file="保存路径"#要/开头，请确保路径文件夹存在
sendkey=""#方糖SendKey填入即可开启推送
cmd=""#可选下载完成后执行的指令
##开始
bdslog=file+"/BDSlog"
if os.path.exists(bdslog):
    print("检测BDSlog文件存在")
else:
    print("检测到BDSlog文件不存在,创建bdslog文件")
    f=open(file+"/BDSlog","w+",encoding='utf8')
    f.close()
f=open(bdslog,"r+",encoding='utf8')
bds=[]
for i in f.readlines():
    bds.append(i.strip())
f.close()
r=requests.get('https://ssk.taiyu.workers.dev/zh-hans/download/server/bedrock')
soup = BeautifulSoup(r.text,'lxml')
print("请求结果："+str(r.status_code))
url=soup.find("a",attrs={"class" :"btn btn-disabled-outline mt-4 downloadlink"}).get("href")
filename=url.split("/")[-1]
print("BDS最新版本："+filename)
up=0
if filename in bds:
    print("文件已存在")
else:
    print("开始下载")
    linux=os.system("wget "+"-t 3 -nv -P "+file+"/linux "+"https://minecraft.azureedge.net/bin-linux/"+filename)
    win=os.system("wget "+"-t 3 -nv -P "+file+"/win "+"https://minecraft.azureedge.net/bin-win/"+filename)
    up=1
    bds.append(filename)
    print("下载完成")
f=open(bdslog,"w+",encoding='utf8')
for i in bds:
    f.write(str(i)+"\n")
    pass
f.close()
##执行脚本
if up==1:
    if cmd:
        r=os.system(cmd)
        if r==0:
            os.system("rm -rf "+file+"/linux/*")
            os.system("rm -rf "+file+"/win/*")
            print("指令执行完成")
    if sendkey:
        data = {"text":"bds脚本执行日志","desp":"BDS最新版本"+filename}
        r=requests.post("https://sctapi.ftqq.com/"+sendkey+".send",data = data)
        if r.status_code==200:
            print("推送成功")
print("全部完成")
