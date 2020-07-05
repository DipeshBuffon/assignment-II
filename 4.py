#Create a list. Append the names of your colleagues and friends to it.
#Has the id of the list changed? Sort the list. What is the first item on
#the list? What is the second item on the list?

lst = []

print(id(lst))

#Appending names of friemds
lst.append("Suraj")
lst.append("Mohan")
lst.append("Aman")
lst.append("Bobby")
lst.append("Jiten")


print(id(lst))  #ID is not changed


#sorting the list
lst.sort()

#first item on the list is:-
print(lst[0])

#Second item in the list is:-
print(lst[1])
