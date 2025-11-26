#LISTS: 
listl = [1, 2, 4, 5, "abc", "hihi",4, 6, 4]
print(list)

listl1 = list() # forms an empty list.

#the list can contain booleans, strings, numbers , almost all datatypes in python. 

#referring to the item :
x = listl[0] #is pulling number '1' from the list.
# a negative index can also be used (logic is same as string slicing.)

#the elements in the list are also iteratable, i.e we can use a list for iteration in a for loop.
for i in listl: 
    print("hihi")

# we can write conditionals wrt to lists as well:
if "abc" in listl: 
    print ("that's nice :)")

#stuff can be added to the list using append"
listl.append("hi")

#we can also specify the index of insertion: 
listl.insert(1, "wasup")

# we can also remove the last items from the list using pop
listl.pop()

# we can also remove a specific item :
listl.remove("wasup")

#all elements can be removed using .clear 
listl.clear
listl = [1, 2, 4, 5, "abc", "hihi",4, 6, 4]

#the list can be reversed using .reverse()
listl.reverse

# the .sort() attribute helps to sort the list in numerical order(lowest to highest, ascending)
listl.sort()

#the list can also be copied onto a new list using the syntax: 
new_listl = sorted(listl)

print(new_listl)

#list elements can be multiplied: 
listl1 = ["hello, good evening!"]* 4
print(listl1)

#lists can be added, 
listl2 = listl1+ listl
print(listl2)

#the list can be accessed from a start to stop index: 
a = listl2[1:4] # a step index can also be added in the form of [start:stop:step]
print(a)

#copying a list using .copy()
listl3 = listl2.copy()
print(listl3)

