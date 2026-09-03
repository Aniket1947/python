
# x=(lambda a:a*a)
# print(x(4))

from functools import reduce
l=[1,2,3,4,5,6,7,8,9]

def evenNumber(n):
    return n%2==0

x=list(filter(evenNumber,l))
print(x)

# x=list(filter(lambda x:x%2==0,l))
# print(x)

# x=list(map(lambda x:x*2,l))
# print(x)

# x=reduce(lambda x,y:x+y,l)
# print(x)
