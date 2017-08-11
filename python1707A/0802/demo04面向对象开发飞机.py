"""
利用面向对象
实现对飞机的控制
游戏面板：
   属性
   方法
我方飞机：
    属性
    方法

"""
import time,pygame
from pygame import locals
#定义游戏面板
class GameMenu():

    def __init__(self):
        self.width=470
        self.heigh=750
        self.image=pygame.image.load("./images/bg.jpg")
    def start(self):
        #创建游戏面板
        screen=pygame.display.set_mode((470,750),0,32)
        plane=Plane(screen)
        #定义一个私有函数，用于进行键盘控制
        self.__key_control(screen,plane)
    def __key_control(self,screen_x,plane):
        while True:
            screen_x.blit(self.image,(0,0))
            #显示飞机
            plane.display()
            for e in pygame.event.get():
                if e.type==locals.QUIT:
                    print("Game Over")
                    exit()
                elif e.type==locals.KEYDOWN:
                    if (e.key==locals.K_a) or\
                    (e.key==locals.K_LEFT):
                        print("<<<<<<<<left")
                        plane.move(-10)
                    elif (e.key==locals.K_d)or\
                            (e.key==locals.K_RIGHT):
                        print(">>>>>>>>>roght")
                        plane.move(+10)
                    elif e.key==locals.K_SPACE:
                        print("开火")
        #渲染游戏背景
            pygame.display.update()
#我方飞机
class Plane():
    def __init__(self,screen_x):
        self.x=150
        self.y=600
        self.image=pygame.image.load("./images/fly.png")
        self.screen=screen_x
    #显示飞机
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    #飞机的移动
    def move(self,speed):
        self.x +=speed

#游戏的入口
if __name__=="__main__":
    game=GameMenu()
    game.start()
