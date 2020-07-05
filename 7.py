#Create a list of tuples of first name, last name, and age for your
#friends and colleagues. If you don't know the age, put in None.
#Calculate the average age, skipping over any None values. Print out
#each name, followed by old or young if they are above or below the
#average age.


lst = [('Shyam','Kc',22),("Manjil","Budathoki",None),("Hari","Gole",41),("Max",'Thapa',55),("Ajay","Ghale",None)]

def calc(l):
    s=0
    n=0
    for i in range(len(lst)):
        if l[i][2]!=None:
            s=s+l[i][2]
            n=n+1
    return(s/n)

avg = int(calc(lst))

for i in lst:
    if i[2]!=None & i[2]>avg:
        print(i[0]+" old.")
    elif i[2]!=None & i[2]<avg:
        print(i[0]+" young.")
