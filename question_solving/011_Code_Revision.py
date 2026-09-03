# Find the given number is prime or not

# def is_prime(n):
#     if n<=1:
#         print(f"{n} is not a prime number")
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 print(f"{n} is not a prime number.")
#                 print(f"{n} is divisible by {i}")
#                 break
#         else:
#             print(f"{n} is a prime number.")

# num=int(input("Enter the Number to check wheather a given number is prime or not."))
# is_prime(num)


	


################################################################################################################

# Sum of n natural number using recursion.

# def sum_n(n):
#     if n<=0:
#         return n
#     elif n==1:
#         return 1
#     else:
#         return n + sum_n(n-1)

# num=int(input("Enter the n number to sum all the number."))
# if num<=0: #This validation check the given number is postive or negative if number is negative this block will excute.
#     print("Enter positive number.")
# else:
#     print(f"The sum of {num} natural number is {sum_n(num)}.")



################################################################################################################



#Sum of n natural number using while loop

# n=int(input("Enter the n number to sum of all number."))

# i=0
# total=0
# while i<=n:
#     total = total+i
#     i=i+1
# print(f"The sum of n natural number is {total}.")

#######################################################################################################

# Fibonacci Series using recursion.

# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)

# n=int(input("Enter the number:"))
# if n<=0:
#     print("Enter a positive number.")
# else:
#     for i in range(n):
#         print(fib(i),end=" ")


##########################################################################################################

#To find the factorial

# def fac(n):
#     if n<=1:
#         return 1
#     else:
#         return n * fac(n-1)

# n=int(input("Enter the Number:"))
# print(f"The Factorial of {n} number is {fac(n)}")


###########################################################################################################

# Reverse the String
# def reverse_String(text):
#     reverse=""
#     for char in text:
#         reverse = char + reverse
#     return reverse

# text=input("Enter the Words you want to reverse:")
# print(f"Reverse String:{reverse_String(text)}")



###############################################################################################################

#Counting vowel present in words

# def counting(text):
#     vowel=['a','i','e','o','u']
#     count=0
#     for char in text:
#         if char.lower() in vowel:
#             count=count+1
#     print(count)

# text=input("Check how many vowel present in words:")
# counting(text)



#############################################################################################################

# def counting(text):
#     vowel=['a','i','e','o','u']
#     count=0
#     word=[]
#     for char in text:
#         if char.lower() in vowel:
#             count=count+1
#             word.append(char)
#         # final="".join(word)
#     print(f"This are the vowel present in words {word} and the total count of vowel is {count}.")

# text=input("Check how many vowel present in words:")
# counting(text)



###################################################################################################

#To check how many times character present in string

# def count_words(text):
#     character='p'
#     count=0
#     for char in text:
#         if char.lower() == 'p':
#             count=count+1
#     print(count)

# text="Pythonp"
# count_words(text)


##################################################################################
#To check the given string is palindrome or not palindrome start from starting or from end string should be same. example "level"

# text=input("Enter the String:")
# if text == text[::-1]:
#     print("Is palindrome")
# else:
#     print("Is not Palindrome")



######################################################################################################

# l=[22,33,44,11,43,5,4,76,88,33,55]

# #Using for loop
# large=l[0]
# for li in l:
#     if li > large:
#         large=li
# print(f"The largest number in list is {large}.")

# print(max(l)) #Direct Approach to get the largest element.


######################################################################################################


# def check_vowel(text):
#     vowel=['a','e','i','o','u']
#     count=0
#     for t in text:
#         if t.lower() in vowel:
#             count=count+1
#     print(count)

# text=input("Enter the Word to check how many vowel char present in:")
# check_vowel(text)

# def check_consonants(text):
#     vowel=['a','e','i','o','u']
#     count=0
#     for t in text:
#         if t.lower() not in vowel:
#             count=count+1
#     print(count)

# t=input("Enter the Words:")
# check_consonants(t)


######################################################################################################



# numbers=[44,2,66,48,87,11,55]
# largest=numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print(largest)

# def largest_number(num):
#     largest=num[0]
#     for number in num:
#         if number > largest:
#             largest = number
#     print(largest)

# numbers=[33,43,2,66,88,44,32,1]
# largest_number(numbers)

######################################################################################################

# import pandas as pd
# numbers=pd.Series([44,66,2,66,48,87,11,55,66,48])
# print(type(numbers))
# print(numbers)
# print(numbers.drop_duplicates())

# numbers=[44,66,2,66,48,87,11,55,66,48]
# new_list=[]
# for num in numbers:
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)

######################################################################################################

# string="Python"
# reverse=""
# for char in string:
# 	reverse= char+reverse
# print(reverse)



######################################################################################################


# def reverse_string(s):
#     if len(s) <=1:
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0]

# text="Python"
# print(reverse_string(text))

#######################################################################################################

# from itertools import permutations

# def permutation(s):
#     return ["".join(p) for p in permutations(s)]

# text=input("Enter the String:")
# p=permutation(text)
# print(f"Orginal String:{text},Permutated String:{p}")

#######################################################################################################

# numberlist=[22,33,44,55,66,77,88,44,33]

# middlelist=int(len(numberlist)/2)
# print(numberlist[middlelist])

#######################################################################################################

# String_list=["P","Y","T","H","O","N"]
# new_string="".join(String_list)
# print(new_string)
# print(type(new_string))

#######################################################################################################
# Adding two list element

#First Approach
# list1=[1,2,3,4]
# list2=[5,6,7,8]

# new_list=[]
# for i in range(len(list1)):
#     new_list.append(list1[i]+list2[i])
# print(new_list)


# Second Approach
# list1=[1,2,3,4]
# list2=[5,6,7,8]

# new_list=[x+y for x,y in zip(list1,list2)]
# print(new_list)



#######################################################################################################

# str1 = "Listen"
# str2 = "Silent"

# str1 = list(str1.upper())
# str2 = list(str2.upper())
# str1.sort(), str2.sort()

# if(str1 == str2):
#     print("True")
# else:
#     print("False")


#######################################################################################################
# print("To check wheather the given word is palindrome or not>>")
# str1=input("Enter the first words:")
# str2=input("Enter the second words:")

# if str1.lower() == str2[::-1].lower():
#     print("Palindrome")
# else:
#     print("Not Palindrome.")

# 2 method
# print("To check wheather the given word is palindrome or not>>")
# str1=input("Enter the Word:")
# if str1.lower() == str1[::-1].lower():
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#######################################################################################################

# str1=input("Enter the String:")
# print(str1.count(" "))  


#######################################################################################################

# Fibnocci Series Using Yield
# def fibonacci():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b

# f1=fibonacci()
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))

#######################################################################################################
# String="Hello World"
# freq={}

# for char in String:
#     if char in freq:
#         freq[char] +=1
#     else:
#         freq[char]=1

# print(freq)


#######################################################################################################
#Best a faster Approach
# l1=[1,2,3,4,5,6,7]
# l2=[2,4,6]
# common=[item for item in l1 if item in l2]
# print(common)

#Using for and if else condition
# l1=[1,2,3,4,5,6,7]
# l2=[2,4,6]
# common=[]
# for l in l1: 
#     if l in l2:
#         common.append(l)
# print(common)


# l1=[1,2,3,4,5,6,7]
# l2=[2,4,6]

# common=list(set(l1) & set(l2))
# print(common)


#######################################################################################################
# star=int(input("Enter the Rows:"))
# for i in range(1,star+1):
#     print("*" * i)

#######################################################################################################


# nested_list = [[1, 2], [3, 4, 5], [6], [7, 8, 9]]
# flatten_list=[]
# for l in nested_list:
#     for j in l:
#         flatten_list.append(j)
# print(flatten_list)

#######################################################################################################

# def sum(n):
#     if n<=1:
#         return n
#     else:
#         return n + sum(n-1)

# num=int(input("Enter the nth number to sum:"))
# print(f"The sum of {num} nth number is {sum(num)}")


# num=int(input("Enter the nth number to sum:"))
# sum=0

# for i in range(num+1):
#     sum=sum+i
# print(f"The sum of {num} nth number is {sum}")
        



#######################################################################################################

# from PyPDF2 import PdfWriter

# merger=PdfWriter()
# pdfs=[]
# n=int(input("Enter the Number of pdf you want to merge:"))

# for i in range(n):
# 	name=input(f"Enter the {i+1} pdf name:")
# 	pdfs.append(name)


# for pdf in pdfs:
# 	merger.append(pdf)


# merger.write("Merged.pdf")
# merger.close()
#######################################################################################################

#Find second largest number

# a=[22,87,65,78,43,87,32,123,123,122]
# if(a[0]>a[1]):
#     max1=a[0]
#     max2=a[1]
# else:
#     max1=a[1]
#     max2=a[0]

# for i in range(2,len(a)):
#     if(a[i] > max1):
#         max2=max1
#         max1=a[i]
#     elif a[i]>max2 and a[i] != max1:
#         max2=a[i]

# print(max2)
#############################################
# new_list=set(a)
# largest=max(new_list)

# new_list.remove(largest)
# print(max(new_list))


#######################################################################################################

# l1=[1,2,3,4,5,6]
# newlist=[x**2 for x in l1]
# print(newlist)

# l1=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# newlist=[x for x in l1 if x%2==0]
# print(newlist)

# from functools import reduce
# l1=[1,2,3,4,5,6]
# new_list=reduce(lambda x,y:x+y,l1)
# print(new_list)


#######################################################################################################

# name=["Aniket","Sameer","Aakash"]
# age=[23,24,27]
# result=dict(zip(name,age))
# print(result)

#######################################################################################################

# string="Hello My name Aniket and i have completed my degree in Bacholer of computer Application"
# words=string.split()
# largest=""

# for char in words:
#     if len(char) > len(largest):
#         largest=char

# print(char)


#######################################################################################################

# name=["Aniket","Sameer","Shivam"]
# age=[23,24,28]
# for n in range(len(name)):
#     new_list=dict(zip(name,age))
# print(new_list)

#######################################################################################################

#find odd even number without using module operator

# x=int(input("Enter the number to check the given number is odd or even:"))
# n=int(x/2)

# if n*2 == x:
#     print("Even Number")
# else:
#     print("Odd Number")
#######################################################################################################

# from operator import itemgetter

# marks={"Aniket":89,"Shivam":78,"Sonu":90,"Vishal":85}


# sorted_dict=dict(sorted(marks.items(),key=itemgetter(1)))
# print(sorted_dict)


#######################################################################################################
#Merging to dictionaries 

# def merge(d1,d2):
#     for key,value in d2.items():
#         d1[key]=value
#     return d1

# marks={"Aniket":89,"Shivam":78,"Sonu":90,"Vishal":85}
# age={'Aniket Varma':23,"Shivam G":34,"Sonu K" :24,"Vishal Y":25}

# print(merge(marks,age))

#######################################################################################################
# Question
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Solution
# def twoSums(nums,target):
#     seen={}
#     for i,num in enumerate(nums):
#         remaining= target - num
        
#         if remaining in seen:
#             return [seen[remaining], i]
#         seen[num]=i

# print(twoSums((1,2,3,4,5,6),5))


#######################################################################################################

#To find a longest word from the data

# def longest_words(text):
#     words=text.split()
#     longest=''
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest

# text="We are learning Python Programming"
# print(longest_words(text))


#######################################################################################################

#Print elements that appear only one time in a list.

# from collections import Counter

# data=["Aniket","Sonu","Aakash","Sameer","Deepak","Aniket","Sonu","Deepak","Sameer"]

# count=Counter(data)

# for c in count:
#     if count[c] == 1:
#         print(c)


#######################################################################################################

# Stack Queue Example

# class stack:
#     def __init__(self):
#         self.s=[]

#     def length(self):
#         return len(self.s)

#     def push(self,value):
#         return self.s.insert(0,value)

#     def peek(self):
#         if len(self.s) == 0:
#             raise Exception("Stack is Empty")
#         else:
#             return self.s[0]

#     def remove(self):
#         if len(self.s) == 0:
#             raise Exception("Stack is Empty")
#         else:
#             return self.s.pop(0)

# stk=stack()

# stk.push(10)
# stk.push(20)
# stk.push(30)
# # print(stk.peek())
# print(stk.remove())
# print(stk.remove())

#Using append method
# class stack:
#     def __init__(self):
#         self.s=[]

#     def length(self):
#         return len(self.s)

#     def push(self,value):
#         return self.s.append(value)

#     def peek(self):
#         if len(self.s) == 0:
#             raise Exception("Stack is Empty")
#         else:
#             return self.s[0]

#     def remove(self):
#         if len(self.s) == 0:
#             raise Exception("Stack is Empty")
#         else:
#             return self.s.pop()

# stk=stack()

# stk.push(10)
# stk.push(20)
# stk.push(30)
# # print(stk.peek())
# print(stk.remove())
# print(stk.remove())
#######################################################################################################
#######################################################################################################