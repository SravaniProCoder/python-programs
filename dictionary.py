x = 5
y = "John"
print(x)
print(y)

#create a function

x = 4      
x = "Sally"  
print(x)

#If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
#Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


#Get a list of the keys:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
#Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
#hange the "year" to 2018:

thisdict = {
  "brand name": "max",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
#Add a color item to the dictionary by using the update() method:

thisdict = {
  "barand name": "puma",
  "model": "Mustang",
  "year": 1998
}
thisdict.update({"color": "red"})
print(thisdict)
#The pop() method removes the item with the specified key name:

thisdict = {
  "brand name": "addidas",
  "model": "maniplating",
  "year": 1999
}
thisdict.pop("model")
#create a pop item
print(thisdict)
thisdict = {
  "brand": "addidas",
  "model": "maniplating",
  "year": 2001
}
thisdict.popitem()
print(thisdict)
#Print all key names in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1981
}
for x in thisdict:
  print(x)
#make a copy of a dictionary with the dict() function:

thisdict = {
  "name": "max",
  "model": "roundiing",
  "year": 2012
}
mydict = dict(thisdict)
print(mydict)
#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "sravani",
    "year" : 2001
  },
  "child2" : {
    "name" : "manasa",
    "year" : 2007
  },
  "child3" : {
    "name" : "sandhya",
    "year" : 2011
  }
}
print (myfamily)
#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "sravani",
  "year" : 2001
}
child2 = {
  "name" : "manasa",
  "year" : 2007
}
child3 = {
  "name" : "sandhya",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)



