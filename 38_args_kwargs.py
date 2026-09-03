def data(*args, **kwargs):
    total=0
    for item in args:
        total += item
    print(total)
    # for key,value in kwargs.items():
    #     print(f"{key}:{value}")
    for key,value in kwargs.items():
        print(f"{key}:{value}")


data(2,3,4,5,6,Aniket=89,Sameer=77)