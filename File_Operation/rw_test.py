# f=open('readme.txt','r+',encoding='utf-8')
# print(f.read())
# f.write('\nqadjijdim')#在完档末尾写入
# f.flush()
# print(f.read())#此时不会打出全部内容，应为光标已经在文档的最后
# f.close()

f=open('readme.txt','r+',encoding='utf-8')
f.truncate(20)
print(f.read())