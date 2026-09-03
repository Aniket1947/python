def generator():
    for i in range(1,51):
        yield i

gen=generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# We can also itreate the yield in for loop 
print("for loop started.")
for i in gen:
    if i <= 15:
        print(i)


# b=(1)
# print(type(b))
# b=(1,)
# print(type(b))
# c=set()
# print(type(c))


    