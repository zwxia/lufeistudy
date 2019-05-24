people = ['yellow','white','black']

def change_people():
    #people = ['黄', '白', '黑']  #不能全部替换修改
    people[0]='黄' #可以对列表的某个值进行操作，同理对象类元组等里的某个值可以修改，字符等不能修改
change_people()
print(people)