# BDS-Auto-download
自动化下载并转存MC服务端
> 现阶段只完成了bds的下载
# 说明
自动从bds官网爬取最新bds版本&下载
- 使用Python3爬取，支持多平台
- 支持调用第三方工具转存文件
- 支持Server酱微信推送（如果希望增加其他平台欢迎找我）
- 解决了bedrock官网禁止服务商ip问题

# 食用说明
1. 需要Python3环境
2. 修改BDS-Auto-download.py中的文件路径
登录[Server酱](https://sct.ftqq.com/)获取SendKey
请确保输入的保存路径存在
执行指令cmd只要在linux上ssh可以执行即可执行(win未测试)
3. 通过宝塔计划任务，linux Crontab定时执行

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
可用于生产环境
本项目禁止商业用途(也不可能有人商业用途吧)，基于GPL3开源
