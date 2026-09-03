# Quiz !
# fruits=["Apple","Banana","Cherry"]
# print(fruits[0])
# fruits[1]="Orange"
# print(fruits)
# print(len(fruits))

# Quiz 2
# l=[1,2,3,4,5,6,7,8,9,10] #Creating list without list comprehension 
# l=[i for i in range(1,11)] #Creating list using list comprehension 
# print(l)
# print(l[1:3])
# print(l[-3:])

# Quiz 3
numbers=[5,2,9,1,7]
numbers.sort()
print(numbers)
numbers.append(10)
print(numbers)
numbers.pop(1) #When you use pop method you have to give index number
print(numbers)
numbers.remove(5) # When you use remove method have to give value which value you want to remove.
print(numbers)


# Quiz 4
# names=["Alice","Bob","Charlie"]
# names.insert(1,"David")
# print(names)

# Quiz 5
# coordinate=(10,20)
# print(id(coordinate))
# print(coordinate[0])
# print(coordinate[1])
# coordinate[0]=5 # It will throw an error because in tuple in cannot change tuple once created
# cord_list=list(coordinate)
# print(cord_list)
# cord_list[0]=50
# coordinate=(cord_list)
# print(coordinate)
# print(id(coordinate))

# Quiz 6
# my_set={1,2,3,3,4}
# print(my_set) #It doesn't return the duplicate value it will give only uniquie value from the set.
# my_set.add(5)
# print(my_set)
# my_set.remove(2)
# print(my_set)

# a={1,2,3,4,5}
# b={3,4,5}
# print(a.union(b)) # output:{1,2,3,4,5}
# print(a.intersection(b)) # output:{3}
# print(a.difference(b)) # output:{1,2}
# print(a.issuperset(b))
# print(b.issubset(a))

# Quiz 7
# student={"Name":"Aniket","Age":20,"Grade":"A"}
# print(student["Name"])
# student["Grade"]="A+"
# print(student.items())
# student["City"]="Delhi"
# print(student)

# friends={"Aniket":"8104258253","Sonu":"9874674829","Sameer":"9899473552"}
# print(friends.keys())
# print(friends.values())
# print(friends.items())
# for key ,value in friends.items():
#     print(key,value)

# Quiz 8
# l=[1,2,33,4,4,5,5,7,6,6]
# print(l)
# s=set(l)
# print(s)
# l=list(s)
# print(l)

# Quiz 9
# products = {"Laptop": 75000, "Phone": 400000, "Tablet": 25000, "Headphones": 5000, "Smartwatch": 12000}

# highest_price = 0
# highest_product = ""

# for product, price in products.items():
#     if price > highest_price:
#         highest_price = price
#         highest_product = product

# print(f"Highest priced product: {highest_product}, Price: ₹{highest_price}")

# Quiz 10
# dict1={"Aniket":65,"Sameer":76}
# dict2={"Sonu":54,"Chirag":55}
# dict1.update(dict2)
# print(dict1)






 