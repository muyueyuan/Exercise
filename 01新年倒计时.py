import pygame  # 调用 pygame 库  这个库需要单独安装 安装很简单cmd命令行 pip  install  pygame
import sys
from pygame.locals import *

import datetime  # 调用时间函数  下面  time 也是时间函数
from datetime import datetime
from datetime import date
from datetime import time
import time
import math  # 调用数学函数

pygame.init()  # 初始化 pygame

size = width, height = 550, 400  # 设置pygame窗口的 宽和高

screen = pygame.display.set_mode(size)  # screen 设置窗口大小是 size
pygame.display.set_caption("何所冬暖")  # 设置窗口顶部的标题

background = pygame.image.load("image/bground1.png").convert()  # 装载背景图片

f1 = pygame.font.SysFont('simsun', 30)  # 设置两个字体 大小 30 和 50 样式  幼圆
f = pygame.font.SysFont('simsun', 50)

text1 = f1.render("距离春节过年还有：", True, (0, 0, 0))  # 设置一个文本框

textrect = text1.get_rect()  # 取得文本框的位置矩形大小
textrect.center = (150, 100)  # 设置文本框中心位置为窗口坐标的 （150，100）的位置

spring = datetime(2023, 1, 22, 0, 0)  # 给定过年正月的具体时间, datetime 可以将参数变为时间格式
while True:
    for event in pygame.event.get():  # 取事件队列中的值如有 QUIT 就推出游戏
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    today = datetime.now()  # 取得现在的时间
    day = (spring - today).days  # 用春节的时间减现在的时间 得到天数
    second = (spring - today).seconds  # 得到秒数
    sec = second % 60  # 分别算出 具体秒数  分钟数 和 小时数
    minute = second / 60 % 60
    hour = second / 60 / 60
    if hour > 24:  # 如果小时大于24就减掉24
        hour = hour - 24
    hour = math.floor(hour)  # 去掉hour 和 minute 的小数部分
    minute = math.floor(minute)

    a = str(day) + "天" + str(hour) + '小时' + str(minute) + "分钟" + str(sec) + "秒" + "\n"
    screen.blit(background, (0, 0))  # 在pygame 窗口上刷上背景图
    screen.blit(text1, textrect)  # 刷上固定文字
    text = f.render(str(a), True, (255, 0, 0))  # 刷上时间数
    textrec = text.get_rect()
    textrec.center = (300, 200)
    screen.blit(text, textrec)
    pygame.display.flip()  # 刷新窗口
    time.sleep(1)  # 停留一秒钟