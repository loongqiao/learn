def makeBold(fn):
    def wrapped():
        return "<b>"+fn()+"<b>"
    return wrapped
#定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>"+fn()+"</i>"
    return wrapped

@makeBold
def test1():
    return "hello world1111"
@makeItalic
def test2():
    return "hello world2222"

@makeBold
@makeItalic
def test3():
    return "hello word33333"

print(test1())
print(test2())
print(test3())