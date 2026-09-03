# empty_set=set()
# print(type(empty_set)) #This is how we can create an empty set.


# cars={"Audi","BMW","Toyata","Hero","Maruti"}
# print(cars)
# print(cars[2]) #This will throw an error beacause set are unordered so we cannot access it by index number.

number={1,2,3,4,5}
number1={4,5,6,7,8}
# print(number)
# number.add(89)
# number.add(77)
# number.pop()
# print(number)
# print(number.issubset(number1))
# number.remove(3333) #This will throw an error because this value is not present in number set
# number.discard(3333) #This will Not throw error because this will remove value only if the value is present is in the set
# print(number.intersection(number1)) #Common element from both set like 4 and 5 in this example
# print(number)
# print(number.union(number1)) #It will take both set element but not return duplicate value
print(number.difference(number1)) #Return a set that contains the items that only exist in set x, and not in set y:
print(number.symmetric_difference(number1)) #Take all element except common element from the set.
number.difference_update(number1)
print(number)
