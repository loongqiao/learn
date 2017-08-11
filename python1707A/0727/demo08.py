class A:
    def eat(self):
        print("吃")
class B(A):
    def play(self):
        print("LOL")
    def walk(self):
        print("去公园散步")
class C(B):
    def walk(self):
        print("散步")
class D(C):
    pass
d=D()
d.eat()
d.play()
d.walk()
