# Security_bot #
由于某种不可抗拒原因


## 功能点 ##
* 可控制机器人发送指定消息（临时补的，懒得写判断）
* 可列出已抓取的内容
* 定时抓取RSS链接内容
* RSS订阅添加
* 可搜索已捕获的内容
* 可手动更新


## 缺陷 ##
* 不是入库的玩意（本人不喜欢写数据库）
忘了（略过）。。。


## 改动点 ##
```python
bot=telebot.TeleBot('BOT_TOKEN')
```

33行和114行的
```python
os.system('python main.py') #如果你在Linux上有多个py环境的话，记得改（这里这么写是因为threading这个有问题，动态导入会报错）
```

## 效果 ##
![](https://s2.ax1x.com/2020/02/16/393dRf.png)

![](https://s2.ax1x.com/2020/02/16/39GYCt.png)

![](https://s2.ax1x.com/2020/02/16/39Go5R.png)

![](https://s2.ax1x.com/2020/02/16/393wz8.png)
