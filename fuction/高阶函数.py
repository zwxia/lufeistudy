def func_1(x,y):
    return x+y

def func_2(m):
    return m*m

print(func_2(func_1(1,2)))  #把函数当参数传入，即为高阶函数