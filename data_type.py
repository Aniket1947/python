# a=4
# print(type(a))
# print(a)

# b=12.2
# print(type(b))
# print(b)


# c="Aniket"
# print(type(c))
# print(c)

# is_boolean=True
# print(type(is_boolean))
# print(is_boolean)

# def gen():
#     for i in range(3):
#         yield i

# g=gen()
# print(next(g))
# print(next(g))
# print(next(g))


#################################################################################################################


# a=5
# b=a
# b=6
# c=5
# print(id(a))
# print(id(b))
# print(id(c))
import copy as cp
a=[10,20,30,40]
b=[50,60,70,80]
c=[a,b]
d=cp.copy(c)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(c[0]))
print(id(d[0]))