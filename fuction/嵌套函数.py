age=18
def func_1():
    age=28
    print("age1=",age)     #28
    def func1_2():
        print("age2=",age) #28 向内到外上一级找
    func1_2()
func_1()

