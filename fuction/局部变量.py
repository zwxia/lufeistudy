
name="cat"  #全局
def chang_name():
    name="dog" #局部
    print("name =",name)#dog

chang_name()
print("real_name =",name)  #cat