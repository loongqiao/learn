"""
封装3.0
"""
class Food:
    def __init__(self,fruit):
        self.__fruit=fruit
    @property
    def get_fruit(self):
        return self.__fruit
    @get_fruit.setter
    def set_fruit(self,fruit):
        self.__fruit=fruit


f=Food("Apple")
print(f.get_fruit)
f.set_fruit="Orange"
print(f.get_fruit)