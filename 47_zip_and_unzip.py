name=["Aniket","Sameer","Aakash"]
age=[23,24,27]

zip_file=zip(name,age)
print(list(zip_file)) #It will zip in the form of name and age ,it will single element from both object from name as well as age.

name1=["Aniket","Sameer"]
age1=[23,24,27]
zip_file1=zip(name1,age1)
print(list(zip_file1)) #As you can see in name there is two element and in age there is three element so from age it will take only 2 element rest of element get ignored.

#Unzipping

data=[("Mumbai","Maharashtra"),("Varanasi","Uttar pradesh"),("Kashi","Uttar pradesh"),("Nashik","Maharashtra")]
city,state=zip(*data)
print(data)
print(city)
print(state)
