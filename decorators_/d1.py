# def display(func):
#     print("ecxecution")
#     # func(a , b)
#     return func
#
#
# @display    # @display => add = display(add)
# def add(a, b):
#     print(a + b)
#
#
# @display
# def sub(a, b):
#     print(a - b)
#
# # add = display(add)
#
#
# add(1, 2)
#
# # sub = display(sub)
# sub(2, 1)

#
# def display(func):
#     print("outer execution")
#     def wrapper(*args, **kwargs):
#         print("inner execution")
#         func(*args, **kwargs)
#         return func
#     return wrapper
#
#
# @display
# def add(a, b, c=0):
#     print(a + b + c)
#
#
# @display
# def sub(a, b, c):
#     print( a - b - c)
#
#
# add(1, 2)
# sub(9, 7, 5)



import time

# print(time)
# def add(a, b):
#     x = time.time()
#     time.sleep(1)
#     print(1)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(a + b)
#     y = time.time()
#     print("total time of execution", y - x)
#     print(x, y)
#
#
# def delay_(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         time.sleep(5)
#         end = time.time()
#         print(end - start)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @delay_
# def add(a, b):
#     print(a + b)
#
# @delay_
# def sub(a, b):
#     print(a - b)
#
#
# add(1, 2)
# sub(2, 4)






