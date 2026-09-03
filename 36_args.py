# def sum(*args):
#     total=0
#     for item in args:
#         total +=item
#     return total

# print(sum(2,3,4,5))

from functools import reduce
def sum(*args):
    new=reduce(lambda x,y:x+y,args)
    if __name__ == "__main__":
        return new

print(sum(2,3,4,5,6,7,8))