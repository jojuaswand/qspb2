# # single inheritance
# class Parent:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#     def add_(self):
#         return self.fname, self.lname
#
#     def disp(self):
#         return "hello"
#
#
# class Child(Parent):
#
#     def __init__(self, fname, lname, mname):
#         super().__init__(fname, lname)
#         self.mname = mname
#
#     def disp(self):
#         return super().disp()
#
#
# c = Child("a","b", "c")

# print(c.add_())
# print(c.disp())
# print(c.__dict__)
# print(c.fname)
# print(c.lname)
# c1 = Parent("a", "b")
# print(c1.__dict__)
# print(c.disp())

# multi level

# class P:
#
#     def disp(self):
#         print("hi im p")
#     class A:
#         a = 10
#
# class C1(P):
#      def d(self):
#         super().disp()
#         print("hi im C1")
#
# class C2(C1):
#     def d1(self):
#         super().d()
#         print("hi im C2")
#
# c = C2()
# print(c.d1())
#
# multiple inheritance
# class P:
#
#     def __init__(self, value):
#         self.value = value
#
#     def display_(self):
#         print("hi im P")
#
# class C1:
#
#     def disp(self):
#         print("hello im C1")
#
# class C2(P, C1):
#     def __init__(self, value):
#         super().__init__(value)
#
#     def d(self):
#         super().disp()
#         super().display_()
#         return "both parents called"
#
#
# c = C2("parents")
# print(c.__dict__)
# print(c.d())

# hierarchical inheritance
#
# class P:
#     def __init__(self, value):
#         self.value = value
#
#
#     def disp(self):
#         print("hello im P")
#
# class C1(P):
#     def __init__(self, value):
#         super().__init__(value)
#
#     def disp(self):
#         super().disp()
#         return "hello i c1"
#
# class C2(P):
#     def __init__(self, value):
#         super().__init__(value)
#
#     def disp(self):
#         super().disp()
#         return "hello im c2"
#
#
# c1 = C1("hi")
# c2 = C2("hello")
# c3 = C1("world")
# print(c1.__dict__)
# print(c1.disp())
# print(c2.__dict__)
# print(c2.disp())
# print(c3.__dict__)

# hybrid inheritance

# class P:
#     def __init__(self, value):
#         self.value = value
#
#
#     def disp(self):
#         print("hello im P")

# class C1(P):
#     def __init__(self, value):
#         super().__init__(value)
#
#     def disp(self):
#         super().disp()
#         print("c1")
#         return "hello i c1"
#
# class C2(P):
#     def __init__(self, value):
#         super().__init__(value)
#
#     def disp(self):
#         super().disp()
#         print("c2")
#         return "hello im c2"
#
# class C3(C1, C2):
#     def __init__(self, value):
#         super().__init__(value)
#
#     def d(self):
#         super().disp()
#         return "hi"
#

# c = C3("hi")
# print(c.d())
# print(C1("hi").disp())

# class A:
#     def __init__(self, name):
#         self.student_name = name
#         print(self.student_name)
#
# class B(A):
#     pass
#
# x = B("name")
# print(x.student_name)
# print(x.__dict__)

# class abs:
#     def __init__(self, name):
#         self.name = name
#
#     def disp(self):
#         return self.name
#
#
# a = abs("name")
# b = a.disp()
# print(b)


