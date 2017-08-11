"""
飞机大战----继承
"""

#导入所需要的模板
import time,random,pygame,sys
from pygame import locals

#定义游戏面板
class GamePhoto():
    def __init__(self):
        self.width=512
        self.heigh=768
        self.image=pygame.image.load("./images/bg.jpg")
        self.plane = None
        self.ef = None
        self.screen=pygame.display.set_mode((512,750),0,32)


    #开始游戏
    def start(self):
        #创建游戏面板
        screen=pygame.display.set_mode((512,750),0,32)
        self.plane=Plane(screen)
        self.ef=EnemyFactory(screen)
        self.ph=Photo(screen,"./images/die.png")

        #定义一个私有函数，用来对键盘的控制
        self.__key_control(screen,self.plane,self.ef,self.ph)

    #键盘控制函数
    def __key_control(self,screen_x,plane,ef_tmp,ph_tmp):
        while True:
            screen_x.blit(self.image,(0,0))
            plane.display()
            #显示敌方飞机
            ef_tmp.product()
            ef_tmp.display()
            #ph_tmp.display()


            #碰撞检测
            self.shoot()
            self.die()
            """if res:
               # ph_tmp.display()
                time.sleep(3)
                sys.exit(0)"""
            for e in pygame.event.get():
                #飞机与键盘的互动
                if e.type==locals.QUIT:
                    exit()
            key_pressed=pygame.key.get_pressed()
            if key_pressed[pygame.K_w]or key_pressed[pygame.K_UP]:
                plane.moves(-10)
            if key_pressed[pygame.K_s]or key_pressed[pygame.K_DOWN]:
                plane.moves(15)
            if key_pressed[pygame.K_a]or key_pressed[pygame.K_LEFT]:
                plane.move(-15)
            if key_pressed[pygame.K_d]or key_pressed[pygame.K_RIGHT]:
                plane.move(15)
            if key_pressed[pygame.K_SPACE]:
                plane.fire()
            time.sleep(0.01)
            pygame.display.update()

    #碰撞检测
    def shoot(self):

        for enemy in self.ef.enemy_list:
            for bullet in self.plane.bullet_list:
                if (bullet.x>=enemy.x)and(bullet.x<=enemy.x+enemy.width)\
                    and((bullet.y>=enemy.y)and(bullet.y<=enemy.y+enemy.heigh)):
                    self.screen.blit(pygame.image.load("./images/boom.png"), (enemy.x, enemy.y))
                    #self.boom(enemy.x,enemy.y)
                    print("死亡")
                    #time.sleep(0)

                    self.plane.bullet_list.remove(bullet)
                    self.ef.enemy_list.remove(enemy)

    def die(self):
        for enemy in self.ef.enemy_list:
            if (enemy.x>self.plane.x-enemy.width+30) and (enemy.x <self.plane.x+65-30) \
                    and( enemy.y >self.plane.y-enemy.heigh+30)and(enemy.y<self.plane.y+38):
                self.screen.blit(pygame.image.load("./images/die.png"), (10, 100))
                #time.sleep(3)
                #sys.exit(0)

                time.sleep(0.05)
                #sys.exit(0)
                return True

    """def boom(self,x,y):
        #screen = pygame.display.set_mode((512, 750), 0, 32)
        boom=pygame.image.load("./images/boom.png")
        self.screen.blit(boom,(x,y))"""

#
class Photo():
    def __init__(self,screen_z,image):
        self.x=20
        self.y=200
        self.screen=screen_z
        self.image=pygame.image.load("./images/die.png")
    def display(self):
        self.screen.blit(self.image,(20,200))
#定义我放飞机类
class Plane():
    def __init__(self,screen_x):
        self.x=200
        self.y=500
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
        elif self.x>=450:
            self.x=450

    def moves(self,speed):
        self.y +=speed
        if self.y<=0:
            self.y=0
        elif self.y>=700:
            self.y=700

    #子弹开火
    def fire(self):
        if len(self.bullet_list)<=5:
            b=Bullet(self.x+25,self.y,self.screen)
            self.bullet_list.append(b)

class Other():
    def __init__(self,x,y,image,screen_tmp,speed,width,heigh):
        #Plane.__init__(self,x,y,image,screen_tmp,speed,width,heigh)
        self.x=x
        self.y=y
        self.image=pygame.image.load(image)
        self.speed=speed
        self.width=width
        self.heigh=heigh
        self.screen=screen_tmp

        # 显示飞机
    def display(self):
        self.screen.blit(self.image,(self.x, self.y))
        # 飞机的移动
    def move(self, speed):
        if speed != 0:
            self.speed = speed

        self.y += self.speed


# 军营！
class EnemyFactory():
    def __init__(self, screen_tmp):
        self.screen = screen_tmp
        self.enemy_list = []  # 兵工厂，造的飞机添加到列表中保存起来


    # 生产飞机
    def product(self):
        rand_no = random.randint(1, 100000)
        if (rand_no > 60000) and (rand_no < 60500):
            # 创建小飞机
            rand_x = random.randrange(0, 400)
            self.__product(rand_x, -36, "./images/ffly.png", 5, 70, 50)
        elif (rand_no > 70000) and (rand_no < 70200):
            # 创建中型飞机
            rand_x = random.randrange(0, 350)
            self.__product(rand_x, -92, "./images/ffly2.png", 3, 150, 100)
        elif rand_no > 99900:
            rand_x = random.randrange(0, 100)
            self.__product(rand_x, -80, "./images/ffly3.png", 1, 490, 330)

            # 私有的创建飞机的方法

    def __product(self, x, y, image, speed, width, heigh):
        enemy =Other(x, y, image, self.screen, speed, width, heigh)
        self.enemy_list.append(enemy)

    # 显示飞机
    def display(self):
        for e in self.enemy_list:
            e.display()
            e.move(0)

    #爆炸
    """def boom(self):
        self.plane=Plane(self)
        for enemy in self.enemy_list:
            for bullet in self.plane.bullet_list:
                if (bullet.x >= enemy.x) and (bullet.x <= enemy.x + enemy.width) \
                        and ((bullet.y >= enemy.y) and (bullet.y <= enemy.y + enemy.heigh)):
                    print("死亡")
                    time.sleep(1)
        self.screen.blit(self.image(self.x,self.y))"""



# 子弹对象
class Bullet():
    def __init__(self, x, y, screen_tmp):
        self.x = x
        self.y = y
        self.screen = screen_tmp
        self.image = pygame.image.load("./images/zidan.png")

    # 显示子弹
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 子弹移动
    def move(self):
        self.y -= 15

    # 子弹边缘判定
    def overflow(self):
        if self.y <= 0:
            return True
        else:
            return False


#游戏的入口
if __name__=="__main__":
    game=GamePhoto()
    game.start()
