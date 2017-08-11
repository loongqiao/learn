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
import time,pygame,time
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
                    elif (e.key==locals.K_s)or\
                            (e.key==locals.K_DOWN):
                        plane.moves(+10)
                    elif (e.key == locals.K_w) or \
                            (e.key == locals.K_UP):
                        plane.moves(-10)


                    elif e.key==locals.K_SPACE:
                        print("开火")
                        plane.fire()
        #渲染游戏背景
            time.sleep(0.01)
            pygame.display.update()
#我方飞机
class Plane():
    def __init__(self,screen_x):
        self.x=150
        self.y=600
        self.image=pygame.image.load("./images/fly.png")
        self.screen=screen_x
        self.bullet_list=[]
    #显示飞机
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for b in self.bullet_list:
            b.display()
            b.move()
            if b.overflow():
                self.bullet_list.remove(b)
    #飞机的移动
    def move(self,speed):
        self.x +=speed
        if self.x<=0:
            self.x=0
        elif self.x>=410:
            self.x=410

    def moves(self,speed):
        self.y += speed
        if self.y<=0:
            self.y=0
        elif self.y>=750:
            self.y=750

    def fire(self):
        if len(self.bullet_list)<=3:
            b=Bullet(self.x+25,self.y,self.screen)
            self.bullet_list.append(b)
#子弹对象
class Bullet():
    def __init__(self,x,y,screen_tmp):
        self.x=x
        self.y=y
        self.screen=screen_tmp
        self.image=pygame.image.load("./images/zidan.png")

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y -=5
    #子弹边缘判定
    def overflow(self):
        if self.y<=0:
            return True
        else:
            return False


#游戏的入口
if __name__=="__main__":
    game=GameMenu()
    game.start()
