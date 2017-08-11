"""
飞机大战V3.0
"""
import pygame,time
from pygame import locals
#创建游戏区域
screen=pygame.display.set_mode((470,750),0,32)
#创建游戏背景区域
back_image=pygame.image.load("./images/bg.jpg")
#创建飞机
fly=pygame.image.load("./images/fly.png")
#位置
x=150

while True:
    #渲染游戏背景
    screen.blit(back_image,(0,0))
    #添加键盘循环的操作
    for e in pygame.event.get():
        if e.type == locals.QUIT:
            exit()#用户点图形界面关闭按钮，结束程序
        elif e.type ==locals.KEYDOWN:#用户按下了按键
            if e.key == locals.K_a or e.key == locals.K_LEFT:
                print("<<<<<<<<<<<<<<<<左左左")
                x-=10
            elif e.key ==locals.K_d or e.key ==locals.K_RIGHT:
                print(">>>>>>>>>>>>>>>>右右右")
                x+=10
            elif e.key ==locals.K_SPACE:
                print("============空格=======")
    screen.blit(fly,(x,600))
    #将所有数据加载到界面
    pygame.display.update()
