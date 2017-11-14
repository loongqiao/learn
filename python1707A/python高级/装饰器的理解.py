# V1.0
# def foo():
#     print('foo')
#
# foo #表示是函数
# foo() #表示执行foo函数

#V 2.0
# def foo():
#     print("foo")
#
# foo=lambda  x:x+1
# foo()

# #v3.0
# def haha(func):
#     print('haha...')
#     func()
#     print('zeze..')
# def hehe():
#     print('hehe...')
#
# haha(hehe)

#V 4.0
'''初创公司有N个业务部门，1个基础平台部门，基础平台负责提供底层的
 功能，如：数据库操作、redis调用、监控API等功能。业务部门使用基础
功能时，只需要调用基础平台的功能即可'''

#5.0
def record(fn):
    def inner():
        print("记录之前")
        fn()
        print("记录之后")
    return inner
def second(fn):
    def inner():
        print("记录之前....")
        fn()
        print("记录之后....")
    return inner

@record
@second
def login():
    print("登陆了...")

#res = record(login)
#res()
login()


# def w1(func):
#     def inner():
#         # 验证1
#         # 验证2
#         # 验证3
#         func()
#     return inner
#
# @w1
# def f1():
#     print('f1')
