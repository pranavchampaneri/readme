# -*- coding: utf-8 -*-              
"""
Created on Sat Aug 13 11:09:30 2022

@author: pranav
"""

#pi = 3.14159
#radius = 2.2
#area = pi*(radius**2)
#print(area)
#hi = "hello there"
#name = input("type your name here")
#print((hi+" "+name +" ")*2)


#x = int(input("Enter your favourite number "))
#print(x)
#x_string=str(x)
#print("my favourite number is", x, ".", "x=", x)
#print("my favourite number is", x_string +".", "x=",x_string)
#print("my fav number is" +" "+ x_string + "." + "x=" + x_string)

#x = float(input("Enter the value for x... "))
#y = float(input("Enter the value for y... "))
#if x == y:
#   print("x + y =", 2*x)
#elif x > y:
#    print("x is greater than y")
#else:
#   print("y is greater than x")
#print("thanks! ")

#x=input("Type anything you wanna achieve in this life...")
#y=input("type the thing you are willing to give up for it...")
#z=int(input("Enter your favourite  number"))

#p= z/2
#q = z%2
#if p ==  0:
#   print("You will never get your",x+", so better get your ass working in order to change your fututre.")
#else:
#   if q == 0:
#        print("Change your way of work, so nothing can stop you from getting your",x+".")
#    else:
#            print("Good going,keep up the good work. You will have your", x, "real soon.")
#elif q == 0:
#    print("You need to change your way of work in order to get your",x + ".")
#else:
#    print("Good going,keep up the good work. You will have your", x, "real soon.")

#print("Try again!")
 

#########
#print("**********\n   :)    \n**********")
#n = input("You are lost in a forest.\nWhich way would you like to go?\nright or left?\n")
#p=1
#while n == "right":
    
#   if p == 2:
#       n = input("You are lost in forest🤦‍♂️.Right or left?")
#    else:
#       p = p+1
#        n = input("You are lost in forest. Which way would you like to go? right or left? Type your response...")
#print("Congratulations! You have found your way out")

########
# code to cheer your word
#an_letters = "aefhilmnorsuxAEFHILMNORSUX"
#word = input("Type the word you wanna get cheered...")
#times = int(input("How excited are you about it on the scale of 1 to 10..."))
#i=0
#while i<len(word):
#    char=word[i]
#    if char in an_letters:
#        print("Give me an "+ char+"! "+char)
#    else:
#        print("Give me a",char+"! ",char)
#    i+=1
#print("What does it spell?")
#for j in range(times):
#    print(word+"!!!")
    
# =============================================================================
# an_letters = "aefhilmnorsuxAEFHILMNORSUX"
# word = input("Type the word you wanna get cheered...")
# times = int(input("How excited are you about it on the scale of 1 to 10..."))
# for char in word:
#     if char in an_letters:
#         print("Give me an "+char+"! ",char)
#     else:
#         print("Give me a ",char+"! ",char)
# print("What do we spell?")
# for j in range(times):
#     print(word+"!!")
# =============================================================================






#guess = 0
#cube = float(input("Type the number of which you need to find the cube root..."))
#epsilon = 0.01
#increment = 0.001
#i = 0
#while abs(guess**3-cube)>=epsilon or guess <= cube:
#   guess = guess + increment 
#    i +=1
    
#guess = guess -  increment
#print("Number of iteration performed = "+str(i))
#if abs(guess**3-cube)>=epsilon:
#    print(str(cube),'is not a perfect cube')
#else:
#    print("The cube root of "+str(cube),"is",str(guess))
    


#cube = float(input("Type the number of which you need to find the cube root..."))
#epsilon = 0.01
#low = 0
#high = cube
#guess = (high + low)/2
#i =0

#for guess in range(int(cube)):
    
#while abs(guess**3 - cube) >= epsilon:
#        if guess**3 == cube:
#            break
#        elif guess**3 - cube < 0:
#            low = guess
#        else:
#            high = guess
#        guess = (high + low)/2
#        i+=1
#print("The cube root of "+str(cube), "is "+ str(guess))
#print ("Nunmber of iteration performed is",i)


#s = "Let's go for a walk, shall we?"
#p = "we will, we will, rock you?"
#i = 0
#for char in p:
#    for char2 in s:
#        if char == char2:
#            i +=1
#            print(i)
#            break


# =============================================================================
# def f(x):
#     """
#     it square the even numbers and cubes the odd numbers
#     """
#     if x%2 == 0:
#         x = x**2
#     else:
#         x = x**3
#     return x
#            
# z = int(input("Insert any whole number"))     
# if z%2 == 0:
#   z = f(z)  
#   print("The number you have entered is even")
#   print("So the square of the enetered number is", z)
# else:
#     z = f(z)  
#     print("The number you have entered is odd")
#     print("So the cube of the entered number is", z)
# 
# 
# =============================================================================
#print(z)



# =============================================================================
# x=3 
# y=4
# print(x*y)
# 
# =============================================================================
# =============================================================================
# =============================================================================
# 


# =============================================================================
# 
#L.extend([7,'Preet'])
# L.pop(2)
# #del(L[2])
# print(L)
# =============================================================================
# =============================================================================
# L= "45n6hh77n8"
# s = L.split ("n")
# print(s)
# =============================================================================


# =============================================================================
# j = ['r','i','s','e']
# p = 'Today'.join(j)
# print(p)
# =============================================================================

# =============================================================================
# Chill = ['Hello', 51]
# Hey = Chill
# Hit = Chill[:]
# Hit.append('there') 	#this will not change Chill
# print(Chill)
# Hey.append("there!")
#print(Chill)
# print(Hit)
# print(Hey)
# =============================================================================
# =============================================================================
# warm = ['red', 'yellow', 'green']
# #warm.sort()
# print(warm)
# #warm.sort(p)
# l = sorted(warm)
# print(l)
# print(warm)
# =============================================================================

# =============================================================================
# def mult_iter (a,b):
#     result = a 
#     while b > 1:
#         result += a
#         b -= 1
#     return result
# x1 = int(input("Enter the first number of which you need product"))
# x2 = int(input("Enter the second number of which you need product"))
# product = mult_iter(x1,x2)
# print("The product of", x1, "and", x2, "is", product)
# =============================================================================


# =============================================================================
#           ## Finding factorial using recursion
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#     
# x = int(input("Enter the number you wish to find factorial of "))
# fact = factorial(x)
# print("The factorial of " + str(x), "is", fact)       
# ========================================================================== 

# =============================================================================
#           #finding factorial using while loop
# x = int(input("Enter the number you wish to find factorial of "))
# fact = 1
# while x >=1:
#     fact = fact * x
#     x -= 1
# print(fact)
# =============================================================================
    
#Recursion
# =============================================================================
# def printmove(fr,to):
#     print("Move form " + str(fr) + " to " + str(to))
# def Towers(n,fr,to,spare):
#     if n == 1:
#         printmove(fr,to)
#     else:
#         Towers(n-1,fr,spare,to)
#         Towers(1,fr,to,spare)
#         Towers(n-1,spare,to,fr)
#         
#         
# =============================================================================

# =============================================================================
# # Fibonacci series
# def fib(n):
#     if n == 1 or n ==0:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# 
# 
# #print(fib(5))
# =============================================================================



# =============================================================================
# class coordinates(object):
#      def __init__(self, x, y):
#          self.x = x
#          self.y = y
#      def distance(self, other):
#          x_diff_sq = (self.x - other.x)**2
#          y_diff_sq = (self.y - other.y)**2
#          return (x_diff_sq + y_diff_sq)**0.5
#      def __str__(self):
#          return ("<"+ str(self.x)+", "+ str(self.y) + ">")
#      def __add__(self,other):
#          return (self.x + other.x, self.y + other.y)
# c = coordinates(3,4)
# origin = coordinates(0,0)
# print(c.y)
# print(origin.x)
# print(c + origin)
# print(c)
# =============================================================================
# =============================================================================
# Name = "Michael Jackson is the best pop star till date."
# N = Name.upper()
# print(N)
# =============================================================================






# =============================================================================
# A = ["banana", 10, 1.2]
# B = A[:]
# A[0] = "hard rock"
# print("A[0]", A[0])
# print("B[0]", B[0])
# =============================================================================

# =============================================================================
# Shop_list = ["watch", "laptop", "shoes", "pen", "clothes"]
# Shop_list.replace('pen', 'notebook')
# print(Shop_list)
# 
# =============================================================================


# =============================================================================
# x = 20 
# def my_function(x):
#       return x
# print(x)
# =============================================================================
# =============================================================================
# c = {}
# string = "Pranav"
# for p,i  in enumerate(string,100):
#     c[p]  = i
#     
# print(c)
# 
# c['name'] = "Champ"
# c['surname'] = 'Champaneri'
# print(c)
# =============================================================================

# =============================================================================
# def printDictionary(**args):
#     print(len(args))
#     for key in args:
#         print(key + " : " + args[key])
#    
# printDictionary(Country='Canada',Province ='Ontario',City ='Toronto')
# =============================================================================


# =============================================================================
# tr ={1:'a', 2:'b'}
# tr.pop(2)
# =============================================================================

# =============================================================================
# f = open("trial.txt", "w")
# f.write("Literature is something you can understand the most when you happen to know the state of author in which he was writing.\nIt isn't necessary to know in every situation")
# f.close()
# 
# f = open("trial.txt", "r")
# print(f.read())
# 
# =============================================================================

# =============================================================================
# 
# import pandas as pd
# songs  = {"Album": ["Thriller", "Black in Black", "Dark side of the mooon"],
#                "Released": [1982, 1980, 1973], "Length": ['42:19', '42:11', '42:49']}
# songs_frame = pd.DataFrame(songs)
# print(songs_frame)
# 
# x = songs_frame[["Album"]]
# print(x)
# 
# =============================================================================


# =============================================================================
# import pandas as pd
# import numpy as np
# import seaborn as sns                       #visualisation
# import matplotlib.pyplot as plt             #visualisation
# #%matplotlib inline     
# sns.set(color_codes=True)
# car_file = "C:\\Users\\prana\\Downloads\\data.csv"
# cars = pd.read_csv(car_file)
# #print(cars.head())
# cars.drop(["Engine Fuel Type", 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis =1)
# cars.head(5)
# cars.shape   #Helps in helps in counting rows aand column
# cars = cars.drop_duplicates()
# cars.head()
# print(cars.shape)
# print(cars.isnull().sum())  #This will show us the number of null values in dataframe
# cars = cars.dropna()
# print(cars.shape)
# print(cars.isnull().sum())
# sns.boxplot(x = cars['Price'])
# =============================================================================


# =============================================================================

with open('Test_file.txt', 'w') as file:
    with open("Test_file1.txt", 'w') as file1:
        for line in file:
            file1.write(line)