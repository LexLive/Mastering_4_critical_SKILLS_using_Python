#Homework 1 - Math operation
'''
first_num = float(input('input first number: '))
second_num = float(input('input second number: '))

print(first_num, '+', second_num, '=' , first_num + second_num)
print(first_num, '-', second_num, '=' , first_num - second_num)
print(first_num, '*', second_num, '=' , first_num * second_num)
print(first_num, '/', second_num, '=' , first_num / second_num)
'''
#Homework 2 Student Grade
'''
st_name = input("Enter the first student's name: ")
st_id = input("Enter the first student's ID: ")
st_grade = float(input("Enter the first student's grade: "))
print('')
nd_name = input("Enter the second student's name: ")
nd_id = input("Enter the second student's ID: ")
nd_grade = float(input("Enter the second student's grade: "))
print('')

print('Informat for students and their "Math" grades')
print(st_name,'(ID ' + str(st_id) +')', 'got grade:', st_grade )
print(nd_name,'(ID ' + str(nd_id) +')', 'got grade:', nd_grade )
print('Average math grade is', (st_grade+nd_grade)/2)
'''

#Homework 3: Even and Odd sum
'''
#a, b, c = map(int, input().split())
odd1, even1, odd2, even2, odd3, even3, odd4, even4 = map(int, input().split())
even_sum = even1 + even2 + even3 + even4
odd_sum = odd1 + odd2 + odd3 + odd4

print(even_sum, odd_sum)
'''


#mine solution
#Homework 4: 
'''
a, b, c = input().split()
print((a+ "'" + b + '"' + c)*10)
'''

#Motafa solution
#Homework4 

A = input()
B = input()
C = input()

combo = A + "'" + B + '"' + C
combo = combo * 10
print(combo)

