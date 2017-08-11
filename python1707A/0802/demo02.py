"""
太空大战V2.0
"""
#引入所需要的模块
import pygame,time
#创建一个游戏区域
screen=pygame.display.set_mode((470,750),0,32)
#创建一个背景图片
back_image=pygame.image.load("./images/bg.jpg")
#创建一个飞机
fly=pygame.image.load("./images/fly.png")
x=150
while True:
    #将图片添加到游戏区域中
    screen.blit(back_image,(0,0))

    #time.sleep(0.001)
    screen.blit(fly,(x,600))

    #将加载的数据渲染到图形界面中
    pygame.display.update()