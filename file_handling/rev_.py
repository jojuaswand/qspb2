# print(print)
# print("hello")
# a = 10
# b = 20
# print(a)
# # print(b)
# print(a, end="#")
# print(b)

# a = 10
# b = 20
# print(a, b)
# print(a, b, sep="$")

# print(10, 20, sep="$#", end="123")
# print(10, sep="$#", end="#")
# print(sep="*", end="#", 10)
# print(10, end="%", sep=" i ")

# a = 10
# print(a.__add__(5))
# print(a.__sub__(5))
# print(a.__divmod__(4))
# print(a.__mul__(4))
# from math import fsum
# print(fsum([a, a]))


# def fun():
#     # return "hello"
#     # return "world"
#     yield "hello"
#     yield "world"
#
#
# # print(fun())
# # print(fun())
# # s = fun()
# # # print(list(s))
# # # for i in s:
# # #     print(i)
# # print(next(s))
# # print(next(s))
# # # print(next(s))
# # print(next)
# # print(next(fun()))
# # for i in fun():
# #     print(i)
# # print(list(fun()))
# # print(fun)
#
#
# def g_(n):
#     for i in range(n):
#         yield i
#
#
#
# # print(g_(5))
# # print(next(g_(5)))
# # print(next(g_(5)))
# # for i in g_(5):
# #     print(i)
# # print(list(g_(5)))
#
#
# s = g_(5)
#
# print(next(s))
# print(next(s))

# for i in range(5):
#     print(i)
# else:
#     print("bye")


# def fun(a, b, c=0):
#     print(a, b, c)
#
#
# fun(1, 2, 3)
# fun(1, 2)
# fun(1)
# print( 2lambda a: a*a)
# a = lambda a: a* a
# print(a(2))
# a = lambda b, c: b*c
# print(a(2, 4))
# # print(a(2))
# print(a)

# import sys
# print(sys.getrecursionlimit())
# print(sys.setrecursionlimit(10))
# print(sys.getrecursionlimit())
# def dis_(i=0):
#     # i = 0
#     if i > 10:
#         return
#     print("executing")
#     i += 1
#     dis_(i)
#
#
# dis_()

# l = [1, 5, 3, 9, 2]
# print(l)
# l.sort()
# print(l)
# l = [9, 5, 4, 10, 1, -1]
# count = 0
# for i, v in enumerate(l):
#     if i + 1 < len(l):
#         if l[i+1] < l[i]:
#             a = l[i]
#             b = l[i + 1]
#             l[i] = b
#             l[i + 1] = a
#             count += 1
#             for i, v in enumerate(l):
#                 if i + 1 < len(l):
#                     if l[i + 1] < l[i]:
#                         a = l[i]
#                         b = l[i + 1]
#                         l[i] = b
#                         l[i + 1] = a
#                         count += 1
#             for i, v in enumerate(l):
#                 if i + 1 < len(l):
#                     if l[i + 1] < l[i]:
#                          a = l[i]
#                          b = l[i + 1]
#                          l[i] = b
#                          l[i + 1] = a
#             for i, v in enumerate(l):
#                 if i + 1 < len(l):
#                     if l[i + 1] < l[i]:
#                         a = l[i]
#                         b = l[i + 1]
#                         l[i] = b
#                         l[i + 1] = a
#                         count += 1
#
# print(l)
# print(count)
# #
# a = 1/4
# for i in range(4):
#     print(f"candy portion given {a}")

# s = {1, 2, 4, "hi", "a"}
# print(s)
# print(frozenset(s))


# def fun_():
#     return "hello"
#     return "bye"
#
#
# print(fun_())
#
# def fun_():
#     yield "hello"
#     yield "bye"
#
#
# print(fun_())
# print(list(fun_()))
# for i in fun_():
#     print(i)
#
# s = fun_()
# print(next(s))
# print(next(s))
# print(next(s))
#
# class Cal_:
#     a = 10
#     b = 4
#     def add_(self):
#         print(self)
#         print(Cal_)
#         return self.a + self.b
#
#     def sub_(self):
#         return self.a - self.b
#
#
# ca = Cal_()
# print(ca.add_())
# # print(ca.__dict__)
# print(Cal_.add_(ca))

from re import *
# txt = "hi hello world"
#
# # r = search("^hi.*d$", txt) #got a match
# # r = search("^hi.*s$", txt) #no match
# # r = search("^hi", txt) #got a match
# # r = search("d$", txt) # got a match
# # r = search("^hi.d$", txt) # no match
# print(1, end=".")
# if r:
#     print("got a match", end="-")
#     print(r.span(), end="- ")
#     print(r.string, end="- ")
#     print(r.group(), end="# ")
#
# else:
#     print("no match", end="#")
#
# s = "hello world"
# d = {}
# for i in s:
#     # d[i] = i
#     # d[0] = i
#
# print(d)


# def fun(a, b=0):
#     return a + b
#
#
# fun(5, 2)
# print(fun(5, 2))

# print(dir(str))
# print(str.__dict__)



