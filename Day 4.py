
day 4
mydict = {
...     101: "prashant",
...     102: "ashish",
...     "103": "mohini",
...     "104":"trivani"
...     }
... print(mydict)
... print(mydict[101])
... for x in mydict.values():
...     print(x)
... ------------------------------------------------------------------------------------------------------------------------------------------
... mydict = {
...     101: "prashant",
...     102: "ashish",
...     "103": "mohini",
...     "104":"trivani"
...     }
... print(mydict)
... print(mydict[101])
... for x in mydict.values():
...     print(x)
... 
... for x, y in mydict.items():
...     print(x, y)
... -----------------------------------------------------------------------------------------------------------------------------------------
... 
... 
... name = "racecar"
... if name == name[::-1]:
...     print("Palindrome")
... else:   print("Not a palindrome")
... 
... ------------------------------------------------------------------------------------------------------------------------------------------
... i = 2, j = 4
... for i in range (2,5):
...     for j in range (4,7):
...         print(i,end=" ")
...     print()


------------------------------------------------------------------------------------------------------------------------------------------
n= (input("enter a number: "))
n = int(n)
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()
-----------------------------------------------------------------------------------------------------------------------------

n=int (input("enter a number: "))
for i in range(1,n+1):
    for j in range(1,1+1):
        print(i,end=" ")
    print()


------------------------------------------------------------------------------------------------------------------------------------------
n= int (input("Enter number of students"))
d={}
for _ in range(n):
    name=input("Enter student name: ")
    marks=int(input("Enter marks: "))
    d[name]=marks
while True:
    name=input("Enter student name to get marks")
    markes=d.get(name,-1)
    if markes != -1:
        print("student not found")
    else:
        print("marks of",name,"are",markes)
        options=input("Do you want to continue? (yes/no)")
        if options.lower() != "yes":
            break
    print("Thank you for using the program") 
