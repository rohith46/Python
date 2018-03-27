#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:04:48 2018

@author: rohithbharatha
"""

input_str = input(" this is my code ")
final_str = input_str.lstrip()
print(final_str)

word=' I love Python programming  '

final_list = word.strip()
print(final_list)

input_list=['SAS','R','PYTHON','SPSS']
input_list.pop(3)
input_list.append('SPARK')
final_list=input_list
print(final_list)

DA_languages = ['R','Python', 'SAS', 'Scala', 42]
DA_languages.append('Java')
print(DA_languages)

input_str='I love Data Science & Python'

output_list =input_str.split('&') 
print(output_list)

input_list =  [['SAS','R'],['Tableau','SQL'],['Python','Java']]
answer = input_list[2][0]
#answer = input_list(3)
print(answer)

word = ['1','2','3','4']

#word[ : ] = []
print(word[ : ])

str_list= ['Pythons syntax is easy to learn','Pythons syntax is very clear']
strp = " & ".join(str_list)
print(type(strp))

input_tuple=('Monty Python', 'British', 1969)
input_tuple=list(input_tuple)
input_tuple.append('Python')
tuple_2= tuple(input_tuple)
# Make sure to name the final tuple 'tuple_2'
print(tuple_2)

input_dict={'Name': 'Monty', 'Profession': 'Singer' }
print(input_dict.get('label'))

input_dict={'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}
print(sorted(input_dict.values()))

list_1=[1,2,3,4,5,6]
list_2=[2,3,4,5,6,7,8,9]
set_1 = set(list_1)
set_2 = set(list_2)
answer_1 = set_1.difference(set_2)
answer_2 = set_1.symmetric_difference(set_2)

print(answer_1)
print(answer_2)

input_str = 'bbbb'

if  input_str[0]== ('a' or 'i' or 'e' or 'o' or 'u') :
    print('YES')
else:
    print('NO')
    
    
if True or True:
    if False and True or False:
        print('A')
    elif False and False or True and True:
        print('B')
    else:
        print('C')
else:
    print('D')
    
    
d = {0: 'Fish', 1: 'Bird', 2: 'Mammal'}
for i in d:
    print(i)
    
d = {0, 1, 2}
for x in d:
    print(d.add(x))

ls = ['wood', 'old', 'apple', 'big', 'item','euphoria']
list_vowel = [word for word in ls if word[0] in 'aieou']

print(list_vowel)
x=6
y=7
def squared(x,y):
     return x**y
#Write your code here

print(squared(x,y))

a = 9
b = 3

greater= lambda a,b : a if a>b else b

print(greater(a,b))
import ast,sys
n = 9
dictionary = {i : i**2 for i in range(1,n+1)}
print(dictionary)
n=4
square_dict = list(num**2 for num in range(1, n+1))
print(square_dict)
ls= ['San Jose', 'San Francisco', 'Santa Fe', 'Houston']
count = map(count, )

print(count)

input_list= [5,6,4,8,9]
def cubes(x):
    return x**3
cube= list(map(cubes,input_list))
print(cube)



list_of_names = ['nikola', 'james', 'albert']
list_of_names2 = ['tesla','watt','einstein']
proper = lambda x, y: x[0]+x[1:] +' '+ y[0]+y[1:]
print(list(map(proper, list_of_names,list_of_names2)))

input_list= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
mulof5 = lambda x:  x % 5 == 0
list_answer = list(filter(mulof5,input_list))
print(list_answer)

from functools import reduce
answer = reduce(lambda x,y: x if x>y else y,input_list)

print(answer)

input_list= ['All','you','have','to','fear','is','fear','itself']

answer= "".join(reduce(lambda x, y: x[0]+x[1:]+' '+ y[0]+y[1:],input_list))

print(answer)

input_list= ['San Jose', 'San Francisco', 'Santa Fe', 'Houston']
fddd = lambda x : x[0] == 'S'
count = len(list(map(fddd,input_list)))

print(count)