from turtle import *

speed(50)
color('red')
pensize(2)

def shape(f, n, size):
    assert n >= 3
    for i in range(n):
        f(size)
        right(360/n)

def repeat_f(num, n, size=20):
    def fn(size=size):
        for i in range(num):
            shape(forward, n, size)
            forward(size)
    return fn

def shape_f(f, n, size):
    def fn(size=size):
        shape(f, n, size)
    return fn

fn = shape_f(repeat_f(6, 3, 10), 4, 20)
shape(fn, 5, 10)
