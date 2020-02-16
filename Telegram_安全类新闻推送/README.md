# Telegram安全新闻推送
- [x] get指令获取列表里的所有更新
- [x] 自动更新文章
- [x] 订阅者可以自己添加RSS进行抓取
- [x] 可列出目前有的RSS
- [x] 可指定搜索db.txt关键字的文章
- [x] 进程守护

# 对应文件的说明
```text
main.py -- 抓取RSS源
bot.py -- Telegram Bot
szk.py -- 生成token
jcsh.py -- 进程守护
rss.txt -- 存放RSS地址
help.txt -- bot帮助信息
key.txt -- token
db.txt -- 抓取到的信息总存
save.txt -- 暂时更新的安全动态
```
# 注意事项
添加RSS源时，请确是如下内容的：
```text
<item><title>Weblogic-T3-CVE-2019-2890-Analysis</title><link>http://xz.aliyun.com/t/6904</link>
```
