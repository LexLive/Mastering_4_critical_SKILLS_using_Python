#str = input()
#print(str)
#print(type(str))

'''
str = input('Enter your name: ')
print('Hello ' + str)
print('Hello ' + input('Enter your name: '))
'''


'''
input()function reads a complete line, and return as string
Let' say you want to read 2 numbers
    - dont't enter both of them on the same line
    - Use 2 input() and input twice (2lines)
'''

'''
a = input('input ')
b = input('input ')

print(int(a) + 2 * int(b))
'''

'''
want to read 3 strings from a single line
'''


'''
a, b, c = input().split()
print(a, b, c)
'''

'''
a, b, c, d = input(int, input).split()
print(b, d)
'''
'''
e, f, g, h = map(int, input().split())
print(g, h)

a, b, c, d, e = map(float, input('Enter 5 numbers: ').split())
'''