# 食用说明
1. 需要Python3环境

需要的模块
```
pip3 install request
pip3 install BeautifulSoup
pip3 install lxml
```

2. 修改BDS-Auto-download.py中的文件路径
登录[Server酱](https://sct.ftqq.com/)获取SendKey

请确保输入的保存路径存在

执行指令cmd只要在linux上ssh可以执行即可执行(win未测试)

3. 通过宝塔计划任务，linux Crontab定时执行
```
python3 BDS-Auto-download.py
```
![](https://img30.360buyimg.com/pop/jfs/t1/144895/2/26774/14176/61d04b8cEeb80388c/55b7dfb2f682072b.png)

可通过以下程序进行转存到onedrive，谷歌网盘，腾讯云cos等
- rclone
- LightUploader

# 未来计划
- 支持多种服务端
- 公共API
- 对接aria2(雾)
# 其他说明
本人邮箱taiyi@qcmoe.com
有问题欢迎反馈，优先邮件解决

本项目禁止商业用途(也不可能有人商业用途吧)，基于GPL3开源
