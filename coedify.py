# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IHHaYJim3j8O3mai2OPsIVYUVTyUheql

Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
"""

inp  = int(input())
sum=0
for i in range(1,inp+1):
  sum += i
print(sum)

"""Modify the previous program such that only multiples of 3 or 5 are considered in the sum.

For example: 3, 5, 6, 9, 10, 12, 15 for n=17
"""

sum=0
for i in range(1,inp+1):
  if i%3==0 or i%5==0:
    sum += i
print(sum)

"""Write a program that takes integer Array of N element and prints sum of even numbers and

sum of odd numbers within the Array.
"""

arr = list(map(int,input().split()))
even = 0
odd = 0
for i in range(0,len(arr)):
  if arr[i]%2==0:
    even+=arr[i]
  else:
    odd+=arr[i]

print("odd",odd)
print("even",even)

"""Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n."""

num = int(input("Enter the number: "))
op = input("Enter operation type (Sum/Product): ")
if op=='Sum' or op=='sum':
  sum=0
  for i in range(1,num+1):
    sum += i
if op=='Product' or op=='product':
  sum=1
  for i in range(1,num+1):
    sum *=i

print(sum)

"""Write a program that prints a multiplication table for numbers up to 12."""

num = int(input('Enter integer: '))
for i in range(1,13):
  print(str(num) +"*" + str(i) + '='+str(num*i))

"""Write a program that checks if a given number N is a prime number or not."""

num = int(input('Enter number: '))
count = 0
for i in range(1,num+1):
  if num%i==0:
    count+=1
if count == 2:
  print("prime number")
else:
  print("Not a prime number")

"""Write a program that prints all prime numbers up to a given number N."""

num = int(input('Enter number: '))
a=[]
for i in range(1,num+1):
  a.append(i)
b=[]
for i in range(0,len(a)):
  count=0
  for j in range(1,num+1):
    if a[i]%j==0:
      count +=1
  if count == 2:
    b.append(a[i])

print(b)

"""Write a function that returns the largest element in a list of Integers."""

a = list(map(int,input('Enter array: ').split()))
a = sorted(a)
print(a[-1])

"""	
Write a function that returns the largest element in a list of strings. Input: ["abc", "xyzaadd", "22", "K", "2dk"] Output: Largest element is: "xyzaadd"
"""

a = list(map(str,input().split()))
result = ""
for i in range(0,len(a)):
  if len(a[i]) > len(result):
    result = a[i]
print(result)

