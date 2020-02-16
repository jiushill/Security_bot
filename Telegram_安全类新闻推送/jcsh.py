#coding=utf-8
#@author:九世
#@time:2019/12/13
#@file:jcsh.py

import os
import time

def jcsh():
    zx=os.popen('ps -elf|grep python3').read()
    if 'python3 bot.py' in zx:
        print('1')
    else:
        dt=time.strftime('%Y-%m-%d %H:%M:%S')
        print('[{}] 发生异常关闭了bot.py'.format(dt),file=open('error.log','a',encoding='utf-8'))
        os.system('python3 bot.py')

    time.sleep(60)

if __name__ == '__main__':
    while True:
        jcsh()