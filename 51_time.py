import time


start=time.time()
for i in range(1000):
    print(i)

end=time.time()

t=0
start1=time.time()
while t<1000:
    print(t)
    t +=1
end1=time.time()
print(end-start)
print(end1-start1)


t=time.ctime()
formatted=time.strftime("%D %H:%M:%S")
print(formatted)
