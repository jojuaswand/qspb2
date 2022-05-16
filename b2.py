# s = "hariharan"
# s1 = ""
# for i in range(len(s)):
#     s1 = s[i] + s1
# print(s1)
# s2 = ""
# i = 0
# while i < len(s):
#     s2 = s[i] + s2
#     i += 1
# print(s2)


# def s_re_(n, s = "", i = 0):
#     while i < len(n):
#         s = n[i] + s
#         i += 1
#     print(s)
#
#
# s_re_("hello")

l = ["yahoo.txt", "google.in", "hi.txt" ]
# l1 = []
# for i in range(len(l)):
#     a = l[i].split(".")
#     if a[1] == "txt":
#         l1.append(l[i])
# l1 = [i for i in l if i.split(".")[1] == "txt"]
# print(l1)

# l = ["google.txt", "hi.in", "bye.txt", "yahoo.in", "hello.txt"]
# l1 = []
# # print("hi.bye".split("."))
# for i in range(len(l)):
#     a = l[i].split(".")
#     if a[1] == "txt":
#         l1.append(l[i])
#         # print(l1)
#     # print(l1)
# print(l1)
# print(l[0].split(".")[1])
# list comprehension
# l1 = [l[i] for i in range(len(l)) if l[i].split(".")[1] == "txt"]
# print(l1)



#appending to a new list
# l = [1, 2, 3, 4]
# l1 = []
# for i in range(len(l)):
#     l1.append(l[i])
# print(l1)

#using list comprehension
# l = [1, 2, 3, 4]
# l1 = [l[i] for i in range(len(l))]
# print(l1)

#only even numbers in new list
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l1 = []
# for i in range(len(l)):
#     if l[i] % 2 == 0:
#         l1.append(l[i])
# print(l1)
#

# using list comprehension
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l2 = []
# l1 = [l[i] for i in range(len(l)) if l[i] % 2 == 0]
# # l1 = [l[i] if l[i] % 2 == 0 else l2.append(l[i]) for i in range(len(l)) ]
# # l1 = [l[i] if l[i] % 2 == 0 else None for i in range(len(l)) ]
# print(l1, l2)

# if element is even square it and if its odd multipy by 2 into a new list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l1 = []
# for i in range(len(l)):
#     if l[i] %2 == 0:
#         l1.append(l[i]**2)
#     else:
#         l1.append(l[i]*2)
# print(l1)

#using comprehension
# l1 = [l[i] ** 2 if l[i] % 2 == 0 else l[i] * 2 for i in range(len(l))]
# print(l1)

#get index and value as tuple and insert to new list
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l1 = []
# for i in range(len(l)):
#     l1.append((i, l[i]))
# print(l1)
# l2 = []
# for i in enumerate(l):
#     l2.append((i[0], i[1]))
# print(l2)
#
# print(list(enumerate(l)))
# print(tuple(enumerate(l)))
# print(str(enumerate(l)))
# print(dict(enumerate(l)))
# print(set(enumerate(l)))
# #using list comprehension
# # l1 = [(i, l[i]) for i in range(len(l))]
# l1 = [(i, v) for i, v in enumerate(l)]
# print(l1)


#if length of string is even append it to new list using normal and comprehension
l = ['hi', 'bye', 'hello', 'good', 'world']
# l1 = []
# for i in range(len(l)):
#     if len(l[i]) %2 == 0:
#         l1.append(l[i])
# print(l1)
#
# l1 =[l[i] for i in range(len(l)) if len(l[i]) % 2 == 0]
# print(l1)
# l1 = [v for i, v in enumerate(l) if len(v) %2 == 0]
# print(l1)

# "hello".split()
# # import math
# # math.trunc()
# # from math import trunc
# # trunc(1.5)
# from math import *
# print(trunc(1.5))
# print(pi)
#


# d = {"name": "balaji", "age": 46, 'place': "chennai"}
# for i in enumerate(d.items()):
#     print(i)
# for i, v in enumerate(d.items()):
#     print(i, v)
#
# for i, (k, v) in enumerate(d.items()):
#     print(i, k, v)
#

# a = 1,2
# print(a)

#if word is starting with and endswith vowel append to new list
# l = ["amazon", "flipkart", "walmart", "gmail", "yahoo", "egg"]
# l1 = []
# for i, v in enumerate(l):
#     if v[0] in "aeiouAEIOU":
#         l1.append(v)
#
# # print(l1)
# l1 = [v for i, v in enumerate(l) if v[0] in "aeiouAEIOU"]
# print(l1)
#
# l2 = []
# for i, v in enumerate(l):
#     if v[-1] in "aeiouAEIOU":
#         l2.append(v)
#
# # print(l2)
# l2 = [v for i, v in enumerate(l) if v[-1] in "aeiouAEIOU"]
#
# print(l2)
# # print("hi")

# print(set())
# print(dict())
#
# a = {}
# print(a, type(a))

# s = "helloworld"
# d = {}
# for i in s:
#     if i in "aeiouAEIOU":
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = ord(i)
#
#
# print(d)

# def add_(a, b):
#     return a + b


# print(add_(10, 5))
# lambda is an anonymous function
# anonymous means without any name
#lambda can take any number of arguements but only one expression
# add two numbers using lambda
# add_ = lambda a, b: a + b
# print(add_(10, 5))
#
# # check whether the given value is odd or even
# evodd = lambda a: "even" if a % 2 == 0 else "odd"
# print(evodd(1111110))

# pal_ = lambda i: "palindrome" if i == i[::-1] else "not a palindrome"
# print(pal_("malayalam"))
# print(pal_("tamil"))

# vo1 = lambda i: "vowel" if i[0] in "aeiouAEIOU" else "not a vowel"
# vo2 = lambda i: "vowel" if i[-1] in "aeiouAEIOU" else "not a vowel"
#
# print(vo1("apple"), vo2("apple"))
# print(vo1("elephant"), vo2("elephant"))

# v = lambda i:"vowel" if i[len(i)//2] in "aeiouAEIOU" else "not a vowel"
#
# print(v("apple"), v("orange"), v("orage"))

# l = [10, 20, 30, 40]
# p = lambda i: i**2
# print(list(map(p, l)))
# print(map)
# print(map(len, "hello"))
# print(list(map(len, "hello")))
# print(list(map(len, ["hello", "hi"])))
# map is a class
# map when called takes two arguements
# 1st arguement is a function name it can be built in function or user defined function
# 2nd arguement should be an iterable object
# map iterates through the iterable object and applies the functionality mentioned
# then it returns a map object which should be either typecasted or iterated to get the final value

# def fun_(a):
#     # l = []
#     for i in a:
#         if i.lower() in "aeiou":
#             l.append(i)
#     # print(l)
#     return l


# fun_("hello")
#
# s = "helloworld"
# a = map(fun_, s)
# # print(list(a))
# # print(list(filter(fun_, s)))
# print(filter)
# print(filter(len, "hello"))
# print(list(filter(len, "hello")))
# print(list(filter(fun_, a)))

# filter is a class
# filter takes two arguements
# 1st arguement is a function name it can be built in function or user defined function
# 2nd arguement should be an iterable object
# filter iterates through the iterable and applies the functionality and returns output as object
# and it also removes None or empty values from the final output
# in user defined function always a return value should be there


# s = "\tha\nk you"
# s = r"\tha\nk you"
# s = r"\\\\"
# s = "\t\n\i"
# print(s)
# a = 1
# b = "boy"
# print("our baby", b, "is", a, "years old")
# print(f"our baby {b} is {a} years old")


# def s_(i):
#     if i <= hundred:
#         print(i)
#         s_(i + one)
#
#
# one = int(True)
# z = int(False)
# hundred = int(f"{one}{z}{z}")
#
# s_(one)


# def fun(x):
#     if x in range(11):
#         print("kgf")
#     elif x in range(11, 21):
#         print("kgf2")
#     else:
#         print("kgf3")
#
#
# fun(1)
# fun(11)
# fun(22)


# def fun_(x, i=0):
#     if i < len(str(x)):
#         print(str(x).replace(str(x)[i], "*"))
#         fun_(x, i+1)
#
#
# a = int(input("enter any number: "))
# fun_(a)

s = "evall is unique question development"
s1 = "evall development question paper"


# def fun_(a, b):
#     s2 = set()
#     s3 = set()
#     l = a.split()
#     l1 = b.split()
#     for i in l:
#         s2.add(i)
#     for i in l1:
#         s3.add(i)
#     print(s2.intersection(s3))
#
#
# fun_(s, s1)

# def pat_(n):
#     for i in range(n):
#         for j in range(n):
#             if i + j == n -1 :
#                 print("*", end=" ")
#             else:
#                 print(" ", end=' ')
#         print()
#
#
# pat_(10)

import time


# def ti_(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(5)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @ti_ # add_ = ti_(add_)
# def add_(a, b):
#     return a + b
#
#
# print(add_(4, 5))

# l = [1, 2.2, 3+3j, "hello", [2, 5], (4, 6), {}, {1,2}]
#
# def ch_(x):
#     c = []
#     ind = []
#     for i in x:
#         if isinstance(i, (str, list, tuple, set, dict)):
#             c.append(i)
#         else:
#             ind.append(i)
#     print(c, ind, sep="--")
#
#
# ch_(l)

# def arc_(*args, **kwargs):
#     print(f"{len(args)} is the number of positional arguements")
#     print(f"{len(kwargs)} is the number of keyword arguements")


# arc_(1, 2, 5, 7, a=6)

# for i in zip("hello", "helloworld"):
#     print(i)

# zip is a class which helps us iterate through two or more objects
# the iteration will stop when the minimum length object reaches empty
# zip returns values from n number of objects inside a tuple


def fun(s):
    if s <= 30:
        print(f"{s} is smaller than 30")
        if s <= 20:
            print(f"{s} is smaller than 20")
            if s <= 10:
                print(f"{s} is smaller than 10")
            else:
                print(f"{s} is greater than 10")
        else:
            print(f"{s} is greater than 20")
    else:
        print(f'{s}, is greater than 30')


# fun(25)
# fun(31)

# Number = int(input(" Please Enter any Number: "))
# Sum = 0
# for i in range(1, Number):
#     if(Number % i == 0):
#         Sum = Sum + i
# if (Sum == Number):
#     print(" %d is a Perfect Number" %Number)
# else:
#     print(" %d is not a Perfect Number" %Number)

#
def pnum(n, sum=0):
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is not a perfect number")


# pnum(int(input("enter number to check: ")))
# print(help("keywords"))

class A:
    a = 10
    __a = 21
    _a = 11


a = 10
b = A()
# print(dir(A))
# print(A._A__a)
x = A._A__a
# print(b._A__a)
# print(A.__class__)
# print(type)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def fun(l):
    l1 = []
    l2 = []
    for i in l:
        if i % 2 == 0:
           l1.append(i)
        else:
            l2.append(i)
    a = sorted(l1, reverse=True)
    from itertools import zip_longest
    new = []
    for i, v in zip_longest(l2, a):
        # if v == None and i == None:
        #     pass
        # # elif i == None:
        # #     pass
        # else:
            new.append(i)
            new.append(v)
    def disp(n):
        return n
    print(list(filter(disp, new)))


# fun(l)

s = "A3B2C4d11c12"
def sc_(x):
    s = ""
    for i in range(len(x)):
        if i < len(x) - 1:
            if x[i+1].isalpha():
                if x[i].isalpha():
                    s = s + x[i]
                else:
                    s = s + str(x[i-1] * (int(x[i]) - 1))
            else:
                if x[i].isalpha():
                    s = s + x[i]
                elif x[i + 1].isnumeric():
                    s = s + str(x[i-1] * (int(x[i]+x[i+1]) - 1))
    print(s)


# sc_(s)

# a = 5
# b = 10
# a, b = b, a
# def ps(func):
#     def wrapper(*args, **kwargs):
#         a = func(*args, **kwargs)
#         return abs(a)
#     return wrapper
#
#
# @ps
# def sub_(a, b):
#     return a - b


# print(sub_(1, 9))

# class Simple:
#     def __init__(self, item):
#         self.item = item
#
#     def __iter__(self):
#         return iter(self.item)
#
#
# s = Simple([1, 2, 3, 4, 5])
# for i in s:
#     print(i)
# print(s.__iter__)
# print(s.__dict__)

# add_ = lambda a, b,c, d, e: a + b - c + d + e
# print(add_(4, 5, 1, 2, 3))

# for i in range(0, 100, 2):
#     print(i)


# a = 65416132
# b = 0
# while a != 0:
#     b = b * 10 + a % 10
#     a //= 10
# print(b)

# l = [-123, 138, -468, 149]
# sump = 0
# sumn = 0
# for i in l:
#     if i < 0:
#         sump += i
#     else:
#         sumn += i
#
# print(sump)
# print(sumn)

# a = "apple"
# b = "orange"
# for i in a:
#     if i in b:
#         print(i)
    # for j in b:
    #     if i == j:
    #         print(j)
l = [1, 2, 4, 1, 5, 2]
# for i in l:
#     if l.count(i) > 1:
#         l.remove(l[str(l).find(str(i))])

# for i in range(len(l)):
#     # for j in range(1, len(l)):
#         if l[i] in l:
#             l.pop(i)
#             break
#
# print(l)
# import time
# for i in range(6):
#
#     for j in range(7):
#         if i == 0 and j % 3 != 0 or i == 1 and j % 3 == 0 or i - j == 2 or i + j == 8:
#             time.sleep(0.5)
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()
#
# for i in range(7):
#     for j in range(7):
#         if i + j >= 6:
#             print(chr(ord("a") + j), end=" ")
#         else:
#             print(" ", end="")
#     print()

print("git")

