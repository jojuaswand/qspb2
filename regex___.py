from re import *
txt = "hi hello world"
#
# r = search("^hi.*d$", txt) #got a match
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
# else:
#     print("no match", end="#")
txt = "hi hello world i hello worl"
txt = "hi hello worl i hello world"
txt = "i hello worl hi d1 hello worl"
r = search("hi.*d", txt)
print(r)


# print(r) # <re.Match object; span=(0, 14), match='hi hello world'>
txt = "hi hello world hi hello world"
# r = findall("^hi.*d$", txt)
# r = findall("^hi", txt)
# r = findall("^hi.d$", txt)
# r = findall("^hi.+d$", txt)
r = findall("hi.*d", txt)
txt = "hi hello world i hello worl"
r = findall("hi.*d", txt)
txt = "hi hello worl i hello world"
r = findall("hi.*d", txt)

print(r)
# print(type(r))


