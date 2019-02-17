#coding=utf-8
"""
@version=1.0
@author:zsh
@file:singleton.py
@time:2019/2/16 20:49
"""
import threading
class SingletonViaAttr(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            origin = super(SingletonViaAttr,cls)
            cls._instance = origin.__new__(cls,*args,**kwargs)
        return cls._instance

def ThreadSyncDecorator(func):
    func.__lock__ = threading.Lock()
    def lock_func(*args,**kwargs):
        with func.__lock__:
            return func(*args,**kwargs)
    return lock_func

class SingletonViaStaticVar(object):
    instance = None
    @ThreadSyncDecorator
    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = object.__new__(cls,*args,**kwargs)
        return cls.instance

class SingletonViaDoubleLock(object):
    __instance = None
    __instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            with cls.__instance_lock:
                if not cls.__instance:
                    cls.__instance = object.__new__(cls,*args,**kwargs)
        return cls.__instance



def testSingle(singleType):
    class MyClass(singleType):
        print(id(singleType))
        a = 1
    first = MyClass()
    second = MyClass()
    print(first.a,second.a)
    print(id(first),id(second))
    print(first==second)
    first.a=2
    print(first.a,second.a)

def x(x):
    return x(x)

def myTrue(a,b):
    return a()
def myFalse(a,b):
    return b()


def myif(judge,func1,func2):
    judge(func1,func2)

if __name__ =='__main__':
    a=1
    b=2
    f1=lambda :1
    f2=lambda :2
    if a>b:
        f1()
    else:
        f2()




    print((lambda x,y:y*x(x,y-1) if y!=2 else 2)(lambda x,y:y*x(x,y-1) if y!=2 else 2,5))
    # for i in range(10):
    #     print('Thread id is {}'.format(i))
    #     t = threading.Thread(target=testSingle(SingletonViaDoubleLock))
    #     t.start()
    #
    # t.join()

