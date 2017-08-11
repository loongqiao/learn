import pygame

from pygame import locals
class GameMenu():
    def __init__(self):
        self.wid=470
        self.hei=750
        self.image=pygame.image.load("./images/bg.jpg")
    def start(self):
        screen=pygame.display.set_mode((self.wid,self.hei),0,32)
        fly=Myfly(screen)
        self.__key_fly(screen,fly)
    def __key_fly(self,screen_tmp,fly):
        while True:
            screen_tmp.blit(self.image,(0,0))
            fly.display()
            for e in pygame.event.get():
                if e.type == locals.QUIT:
                    exit()
                elif e.type == locals.KEYDOWN:
                    if e.key == locals.K_a:
                        fly.move(-10)
                    elif e.key==locals.K_d:
                        fly.move(10)
                    elif e.key==locals.K_SPACE:
                        print("==========")
            pygame.display.update()
class Myfly():
    def __init__(self,screen_tmp):
        self.x=150
        self.y=200
        self.image=pygame.image.load("./images/fly.png")
        self.screen=screen_tmp

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self,speed):
        self.x +=speed
if __name__=="__main__":
    game=GameMenu()
    game.start()