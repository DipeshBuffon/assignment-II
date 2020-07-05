#Create a list with the names of friends and colleagues. Search for the
#name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.


list = ['Sachin', "Kuldeep", "Bigyan", "John", "Hari", "Shyam"]

for name in list:
    if name == 'John':
        print("John is present in the list.")
        break

else:
    print("Not found!!!")
