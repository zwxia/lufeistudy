#匿名函数lambda，支持最复杂的运算就是3元运算

func=lambda x,y:x+y #匿名函数
print(func(2,3)) #5

func2=lambda m,n: m-n if m>n else m+n
print(func2(3,5))#8
print(func2(5,3))#2

an=[0,1,2,3,4,5]
print(len(an))
for i in range(len(an)):
    j=an[i]
    an[i]=j*j
print(an)