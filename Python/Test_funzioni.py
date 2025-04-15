#test utilizzo delle funzioni e visibilità

def f(x):
    def g():
        x='abc'
        print('x -',x)
    def h():
        z=x
        print('z -',z)
    x = x+1
    print('x -',x)
    h()
    g()
    print('x -',x)
    return h

x=3
y=f(x)
print('x -',x)
print('y -',y)
y()
