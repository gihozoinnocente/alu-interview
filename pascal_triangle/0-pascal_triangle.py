#!/usr/bin/python3
"""a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal's triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer """
def printPascal(n):
    """Comment"""
    for i in range(n+1):
        c=1
        for j in range(1, i+1):
            print(c, sep=' ', end='')
            c=c*(i-j)//j
        print()
#driver code
n = int(input("num: "))
printPascal(n)
