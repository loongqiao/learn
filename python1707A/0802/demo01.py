"""
飞机大战游戏V1.0
"""
#导入所需要的模块
import pygame

#创建游戏区域
screen=pygame.display.set_mode((480,853),0,32)

#创建一个背景图片
back_image=pygame.image.load("./images/bg.jpg")

while True:
    #将图片添加到游戏区域中
    screen.blit(back_image,(0,0))
    #将加载的数据，渲染到图形界面中
    pygame.display.update()