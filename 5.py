#Create a tuple with your first name, last name, and age. Create a list,
#people, and append your tuple to it. Make more tuples with the
#corresponding information from your friends and append them to the
#list. Sort the list. When you learn about sort method, you can use the
#key parameter to sort by any field in the tuple, first name, last name,
#or age.
import operator
t1 = ('Dipesh','Adhiakri',21)
people = []
people.append(t1)
t2=("Aman","Mahaseth",24)
t3=("Jerry","Thapa",19)
t4=("Eric","Nepal",28)
people.append(t2)
people.append(t3)
people.append(t4)


print(people.sort(key=operator.itemgetter(0)))
