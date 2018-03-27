#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:45:29 2018

@author: rohithbharatha
"""

#my_string = "Mary had a little lamb"
#for alphabet in my_string:
  #  print(alphabet)
    
str1=''
for i in range(0,9):
    if i<5:
        str1 +='* '
        print(str1)
    elif i>4:
        str1=str1[:-2]
        print(str1)

mystring= 'Mary had a little lamb'
for n,alphabet in enumerate(mystring):
    print(alphabet,n)
    
vowels=''
for alphabet in mystring:
    if alphabet in 'aeiou':
        vowels += ' '+alphabet
print(vowels)

nums = '838848237890237388221'
oddnums=''
evennums=''
for number in nums:
    if int(number)%2 == 0:
        evennums += number
    else:
        oddnums += number
print("Even numbers are: "+ evennums +"\nodd numbers are: " + oddnums)



list_of_inventories = ['Apple', 'Banana', 'Potato', 'Mango', 'Onion', 'Toothpaste']
fruits = ['Apple','Banana','Mango','Orange','Strawberry']
vegetables = ['Potato', 'Onion','Cucumber', 'Celery']

fruits_count=0
vegetables_count=0
print("These are our inventories: ")
for items in list_of_inventories:
    print(items)
    if items in fruits:
        fruits_count+=1
    elif items in vegetables:
        vegetables_count+=1
print("Number of fruits are: ",fruits_count)
print("Number of vegetables are: ",vegetables_count)

sentence = "Is Python simpler than R ?"
for word in sentence.split():
    print(word)
    
#sentence check
tweet = '#beautiful #morning it is looking good'

for word in tweet.split():
    if word.startswith("#"):
       print(word[1:])


students_data = {1:['Shivam Bansal', 24] , 2:['Udit Bansal',25], 3:['Sonam Gupta', 26], 4:['Saif Ansari',24], 5:['Huzefa Calcuttawala',27]}
count=0
for key,value in students_data.items():
    if value[1]<25:
        count+=1
    print(value[1])
print(count)

start=0
total=0

while start<5:
    start+=1
    total+=start
    print(start)
print(total)
