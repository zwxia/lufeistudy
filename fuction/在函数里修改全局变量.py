
name="cat"  #全局
def chang_name():
    global name  #在函数里修改全局变量
    name="dog"
    print("name =",name)#dog

chang_name()
print("real_name =",name)  #dog