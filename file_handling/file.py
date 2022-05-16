path = r"C:\Users\jojua\PycharmProjects\qspb2\file_handling\file1"

# file = open(path, "r")
# print(file.read())
# file.close()

# with open(path, "r") as file_:
#     # print(file_.read())
#     a = file_.read()
#     print(a, type(a))


# with open(path, "w") as file_:
#     print(file_.write("hello  written"))


# with open(path, "a") as file_:
#     print(file_.write("bye written"))


# with open(r"C:\Users\jojua\PycharmProjects\qspb2\file_handling\file2", "x") as file_:
#     print(file_.read())
#
#



# s = "hello"
# s1 = ""
# for i in s:
#     s1 = i + s1
#
# print(s1)
#
# l = ["hello", "bye"]
# l1 = []
# # for i, v in enumerate(l):
# #     l1.append(v[:: -1])
#
# for i in l:
#     l1.append(i[::-1])
#
# print(l1)


# path = r"C:\Users\jojua\PycharmProjects\qspb2\file_handling\file1"

# with open(path, "r") as file_:
#     # print(file_.read())
#     print(file_.tell())
#     print(file_.readline())
#     print(file_.tell())
#     print(file_.readlines())
#     print(file_.tell())
#     print(file_.seek(0))
#     print(file_.read())
#     print(file_.seek(6))
#     print(file_.read())

path = r"C:\Users\jojua\PycharmProjects\qspb2\file_handling\file1"

# with open(path, "r") as file_:
#     l = []
#     for i in file_:
#         # i.strip(r"\n")
#         # if i.strip():
#         l.append(file_.readline())
#     print(l)
# from collections import Counter
# with open(path,"r") as file_:
#     l = []
#     for i in file_:
#         # i = i + " "
#         # print(i)
#         a = i.split()
#         for j in a:
#             l.append(j)
#     print(l)
#     x = Counter(l)
#     print(x)
#     print(Counter)

#
# with open(path, "r+") as file_:
#     l = []
#     for i in file_:
#         a = i.split()
#         for j in a:
#             l.append(j.replace("e", "x"))
#             # l.append(j)
#
#     print(l)
#
#
# from itertools import islice
# with open(path) as file_:
#
#     # a = islice(file_, 1, 8)
#     # print(list(a))
#
#     # a = islice(file_, 1, 8, 2)
#     # print(list(a))
#
#     a = reversed(list(islice(file_, 1, 8)))
#     print(list(a))
#
#     print(reversed)
#

from collections import deque
# with open(path) as file_:
#     # a = deque(file_)
#     # a = deque(file_, 3)
#     # a = deque(file_, 4, 1)TypeError: deque() takes at most 2 arguments (3 given)
#     print(a)

