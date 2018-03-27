#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:40:01 2018

@author: rohithbharatha
"""
rohith1="some thing boy"
print(rohith1.lstrip("s"))
print(rohith1.lstrip("thing"))
print(rohith1.lstrip("some"))
rohith1
print(rohith1.strip("some boy"))
print(rohith1.strip("thing"))

nar = '5 apples'
what= nar[2:4]         
print(what)

no=nar[0:6]         
print(no)

nums=[1,2,3,4,5,6,7,8,9,10]         
print(nums)         
print(nums[4])

number='123456789'         
print (type(number))        
print(number)
even_numbers=number[1::2]
number='123456789'         
print (type(number))         
print(number)
even_numbers=number[1::2]

print(even_numbers)
number = '12345678910'
print(number[::-1])
print(number[1:2])
print(number[1::2])
print(number[0::2])
print(number[0::3])
number = '0123456789'
number[1::2]
number[0::2]
number[0::3]
A= "data"
b= "Analysis"
c= "pandas"
print(A,b,c)
print(" {0} {1} using {2}".format(A,b,c))
print(" {0} {2} using {1}".format(A,b,c))

a='rock'
b='paper'
c='scissors'
print(a,b,c)
print("{1} {2} {0}".format(a,b,c))
a='rock'

b='paper'

c='scissors'

print("{1} {2} {0}".format(a,b,c))
print("{1}{2}{0}".format(a,b,c))
print("{1}{2}{0}",format(a,b,c))
bio_data = {'Name': 'Bob Marley', 'Age':35, 'Height':"5.6 ft", 'Hobby': 'Music'}
print(bio_data)

bio_data = {'Name': 'Bob Marley', 'Age':35, 'Height':"5.6 ft", 'Hobby': 'Music'}
print(bio_data)


name=bio_data['Name']
print(name)
hobby=bio_data['Hobby']
print(hobby)
hobby=bio_data['Hobby','Cricket']
hobby=bio_data.get['Hobby']
age = bio_data['Age']
print(age)

age = bio_data.get['Age']
print(age)

age = bio_data.get()['Age']
print(age)

age = bio_data.get(['Age'])
print(age)

age = bio_data['Age']
print(age)

profession  =  bio_data.get('Profession','NA')
print(profession)

bio_data
print(bio_data)
bio_data['Hobby']='Cricket'
print(bio_data)
print(hobby)
hobby=bio_data['Hobby']
print(hobby)
bio_data['profession']='singer'
print(bio_data)
print('profession' in bio_data)
guess='profession' in bio_data
print(guess)
print(list(bio_data.keys()))
print(list(bio_data.values()))
bio_data['Age']=36
print(list(bio_data.values()))
new_dictionary = dict(Country='Jamaica', Songs=['One Love','Misty Morning'])
bio_data.update(new_dictionary)
print(bio_data)
del bio_data['songs']
del bio_data['Songs']
print(bio_data)
students_data = { 1:['Shivam Bansal', 24] , 2:['Udit Bansal',25], 3:['Sonam Gupta', 26], 4:['Saif Ansari',24], 5:['Huzefa Calcuttawala',27]}

print(students_data)

print(len(students_data))
print(students_data.values())
print(list(students_data.values()))
print(list(students_data.keys()))
students_data[6]=['Mansal',24]
print(students_data)
del students_data[2]
print(students_data)
print(list(students_data))
print(list(students_data.values()))
print(list(students_data.keys()))

small = "i am upper cased"
print(small.upper())

large = "I AM LOWER CASED"
print(large.lower())

batch = "5 oranges 3 monkeys n"

print('we have ', batch[:-3])
batch = "5 oranges 3 monkeys n"

print('we have ', batch[:-3])
#we have  5 oranges 3 monkey

batch = "5 oranges 3 monkeys n"

print(batch[2:9]) #fruits
#oranges

print(batch[10:-2]) #animals
#3 monkeys

print(batch[10:-3]) #animals
#3 monkey

print(batch[11:-2]) #animals
# monkeys

print(batch[12:-2]) #animals
#monkeys

print(batch[::-2])
#nsenm3sgao5

print(batch[::-1])
#n syeknom 3 segnaro 5

print(batch[5::])
#nges 3 monkeys n

print(batch[5:])
#nges 3 monkeys n

nums = '123456789'

odd_nums_again = nums[ :: 2]

print(odd_nums_again)
#13579

odd_nums_again = nums[ :: 3]

print(odd_nums_again)
#147

odd_nums_again = nums[ 1:: 2]

print(odd_nums_again)
#2468

master="Electrical and Computer Engineering"

time=2

print("i did my education in {0} for {1}years".format(master,time))

#i did my education in Electrical and Computer Engineering for 2years

x=2

y=3

print("addition of {0} and {1} is 5".format(x,y))
#addition of 2 and 3 is 5

print("addition of {1} and {0} is 5".format(x,y))
#addition of 3 and 2 is 5

firstname='monty'

lastname='python'

name=firstname+" "+lastname

print(name)
#monty python

age=27

my_age='my age is {0} years old'.format(age)

print(my_age)
#my age is 27 years old

name +=my_age

print(name)
#monty pythonmy age is 27 years old

name +=" "+my_age

print(name)
#monty pythonmy age is 27 years old my age is 27 years old


print(name)
monty pythonmy age is 27 years old my age is 27 years old

name -=my_age
Traceback (most recent call last):

  File "<ipython-input-246-c5850606627d>", line 1, in <module>
    name -=my_age

print(name)
#monty pythonmy age is 27 years old my age is 27 years old

name = 'monty python'

my_age='my age is {0} years old'.format(age)

name += ' '+my_age

print(name)
#monty python my age is 27 years old

DA_languages = ['R','Python', 'SAS', 'Scala', 42]
DA_languages.append('Java')


print(DA_languages)
#['R', 'Python', 'SAS', 'Scala', 42, 'Java']

DA_languages.pop()
#Out[257]: 'Java'

print(DA_languages)
#['R', 'Python', 'SAS', 'Scala', 42]

DA_languages.pop(0)
#Out[259]: 'R'

print(DA_languages)
#['Python', 'SAS', 'Scala', 42]

DA_languages.pop(-1)
#Out[261]: 42

print(DA_languages)
#['Python', 'SAS', 'Scala']

DA_languages.append('R')

print(DA_languages)
#['Python', 'SAS', 'Scala', 'R']

DA_languages.append('R')

DA_languages.remove('R')

print(DA_languages)
#['Python', 'SAS', 'Scala', 'R']

DA_languages.remove('R')

print(DA_languages)
#['Python', 'SAS', 'Scala']

print(DA_languages.append('R'))
#None

print(DA_languages)
#['Python', 'SAS', 'Scala', 'R']

print(id(DA_languages))
#4676247240

new_list = DA_languages[:]

print(id(DA_languages))
#4676247240

print(id(new_list))
#4676372168

a_sentence = "Hi Saif, this is to inform you that I'm not well today."

print(a_sentence.split())
#['Hi', 'Saif,', 'this', 'is', 'to', 'inform', 'you', 'that', "I'm", 'not', 'well', 'today.']

print(a_sentence.split(','))
#['Hi Saif', " this is to inform you that I'm not well today."]

sentences=a_sentence.split(',')

print(sentences)
#['Hi Saif', " this is to inform you that I'm not well today."]

mail=" ".join(sentences)

print(mail)
#Hi Saif  this is to inform you that I'm not well today.

print(mail)
#Hi Saif  this is to inform you that I'm not well today.

mail=",".join(sentences)

print(mail)
#Hi Saif, this is to inform you that I'm not well today.

nums = [2,6,9,3,2,1]

sorted(nums)
#Out[288]: [1, 2, 2, 3, 6, 9]

max(nums)
#Out[289]: 9

min(nums)
#Out[290]: 1

print(len(nums))
#6

nest = [[1, 2, 3, 4], [ 5, 6, 7], [8, 9, 10]]

print([1])
#[1]

print(nest[1])
3[5, 6, 7]

print(nest[0:1])
#[[1, 2, 3, 4]]

print(nest[0:2])
#[[1, 2, 3, 4], [5, 6, 7]]

print(nest[0:3])
#[[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

print(nest[0][1])
#2

print(nest[1][2])
#7

print(nest[1][2])
#7

print(nest[2][1])
#9