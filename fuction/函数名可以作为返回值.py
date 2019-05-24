def func_1():
    print('ceshi')
    return func_1
var=func_1()
#var()  会再次调用func_1()
