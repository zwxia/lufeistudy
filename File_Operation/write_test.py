fi=open(file="readme.txt",mode="w",encoding="utf-8") #w模式write会清空文件内容写入新的
fi.write('测试写入')
fi.close()


fi=open(file="readme.txt",mode="a",encoding="utf-8")#a 追加模式，在最后行加
fi.write('\n测试写入1')
fi.close()