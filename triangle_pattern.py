from turtle import *

def triangle(size=200):
    for i in range(3):
        forward(size)
        left(120)

def triangle_line(n=10, size=100):
    for i in range(n):
        triangle(size)
        forward(size)

def triangle_square(n=10, size=100):
    for i in range(4):
        triangle_line(n, size)
        right(90)

triangle_square(5, 100)

input('...')
