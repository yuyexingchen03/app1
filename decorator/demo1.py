#!/usr/bin/env

def log(f):
    def fn(*args,**kwargs):
        print(f.__name__,'---->running')
        return f(*args,**kwargs)
    return fn

'''
使用@log装饰器类似
    def testdec(f):
        def fn(*args,**kwargs):
            print(f.__name__,'---->running')
            return f(*args,**kwargs)
        return fn
        
    def test(x,y):
        return  x+y
        
    test = testdec(test)
'''
@log
def test(x,y):
    return  x+y

if __name__ == '__main__':
    x = test(2,5)
    print('x------>>>',x)

