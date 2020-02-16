#@author:九世
#@time:2019/12/11
#@file:bot.py

import telebot
import time
import threading
import os
import re

bot=telebot.TeleBot('BOT_TOKEN')

@bot.message_handler(commands=['help'])
def helps(message):
    dta=''
    helps=open('help.txt','r',encoding='utf-8')
    for u in helps.readlines():
        dta+=u
    bot.reply_to(message,dta)

@bot.message_handler(commands=['list'])
def lptst(message):
    dta=''
    helps=open('db.txt','r',encoding='utf-8')
    for u in helps.readlines():
        dta+=u
    sulited_text=telebot.util.split_string(dta,3000)
    for text in sulited_text:
        bot.reply_to(message,text)

@bot.message_handler(commands=['update'])
def updates(message):
    os.system('python main.py')
    dta=''
    helps=open('save.txt','r',encoding='utf-8')
    for u in helps.readlines():
        dta+=u

    if len(dta)>0:
        sulited_text = telebot.util.split_string(dta, 3000)
        for text in sulited_text:
            bot.send_message(631202355, text)
    else:
        bot.reply_to(message, '没有新的动态')

@bot.message_handler(commands=['rss_list'])
def rss_list(message):
    dta=''
    helps=open('rss.txt','r',encoding='utf-8')
    for u in helps.readlines():
        dta+=u
    sulited_text=telebot.util.split_string(dta,3000)
    for text in sulited_text:
        bot.reply_to(message,text)

@bot.message_handler(regexp="[/]add [0-9-a-z]{32}.*[>][a-zA-z]+://[^\s]*")
def add_rss(message):
    text=str(message.text)
    bvg=re.findall('[/]add [0-9-a-z]{32}.*[>][a-zA-z]+://[^\s]*',text)
    if len(bvg)>0:
        token=re.findall('[0-9-a-z]{33}',text)
        if len(token)>0:
            tokens=str(token[0]).replace(' ','').rstrip().lstrip()
            keyslist=[]
            rsslists=''
            dk=open('key.txt','r',encoding='utf-8')
            for v in dk.readlines():
                data="".join(v.split('\n'))
                keyslist.append(data)

            dk2 = open('rss.txt', 'r', encoding='utf-8')
            for v in dk2.readlines():
                rsslists+=v


            if tokens in keyslist:
                da=text.split(' ')[-1].split(' ')[-1]
                link=da.split('>')
                if str(link[1]) not in rsslists and str(link[0]) not in rsslists:
                    print('{}'.format(da),file=open('rss.txt','a',encoding='utf-8'))
                    bot.reply_to(message,'已成功添加:{}'.format(da))
                else:
                    bot.reply_to(message,'RSS源已存在:{}'.format(link[-1]))
            else:
                bot.reply_to(message,'没有这个token,非内定者无法添加RSS源')
        else:
            bot.reply_to(message,'请输入token')
    else:
        bot.reply_to(message,'输入格式不正确')

@bot.message_handler(regexp="[/]sendhaq .*")
def sends(message):
    dt=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    data='[{}] Admin:{}'.format(dt,str(message.text).replace('/sendhaq','').lstrip().rstrip())
    sulited_text = telebot.util.split_string(data, 3000)
    for text in sulited_text:
        bot.send_message(631202355, text)

@bot.message_handler(regexp="[/]search .*")
def searchs(message):
    searchs=str(message.text).replace('/search','').lstrip().rstrip()
    texts=''
    helps = open('db.txt', 'r', encoding='utf-8')
    for u in helps.readlines():
        if searchs in u:
            texts+=u

    sulited_text=telebot.util.split_string(texts,3000)
    for text in sulited_text:
        bot.reply_to(message,text)


def start():
    os.system('python main.py')
    dta = ''
    helps = open('save.txt', 'r', encoding='utf-8')
    for u in helps.readlines():
        dta += u

    if len(dta) > 0:
        sulited_text = telebot.util.split_string(dta, 3000)
        for text in sulited_text:
            bot.send_message(631202355,text)

    print('bot开始工作')
    '''
    如果运行机器人，发生超时错误的话，还是会继续运行的，但是加了
    bot.stop_bot()就很不行，玄学问题...
    '''
    try:
        bot.polling()
    except Exception as r:
        print('Error:{}'.format(r))

while True:
    try:
        t=threading.Thread(target=start,args=())
        t.setDaemon(True)
        t.start()
        t.join(600)
    except:
        pass