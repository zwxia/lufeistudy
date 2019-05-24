def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print ("[DEBUG]: enter {}()".format(func.__name__))
        print ('Prepare and say...',)
        func(*args, **kwargs)
    return wrapper  # 返回

@debug
def say(something):
    print ("hello {}!".format(something))

@debug #say_hello = debug(say_hello)
def say_hello():
    print ("hello!")

@debug
def say_goodbye():
    print ("hello!")

say_hello()
say_goodbye()
say(1234565432345)