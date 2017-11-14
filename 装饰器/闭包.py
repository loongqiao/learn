def test1():
    print("---in test func----")

#调用函数
test1()

#引用函数
ret=test1

print((id(ret)))
print(id(test1))

#通过引用调用函数
ret()
