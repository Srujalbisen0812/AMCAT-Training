#Q1

#WAP to acceot any one digit and check pos , neg and zero

no = int(input("Enter any one number :"))

if no>0:
    print("no is positive:")

if no<0: #rational 
    print("no is negtive")

if no == 0: #compartive operator
    print("zero")

````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#Q2

#WAP to accept days and check working day and weekend 

day =input("Enter the day: ")

if day == "saturday" or day=="sunday" or day =="SATURDAY" or day=="SUNDAY":
    print("It's a weekend")

else:
    print("working day")

````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#Q3
#WAP to acccept three paper marks and calculate total marks , percentage and check if percentage is greater then or equal to 60 the he/she is eligible for placement.

physics =int(input("enter the marks physics: "))
chemistry = int(input("enter the marks chemistry:"))
maths = int(input("enter the marks of maths :"))

total= physics+chemistry+maths
percentage = total/3.0
print("total =",total)
print("percentage=",percentage)

if percentage>=60:
    print("the student is eligible for placement." "first class")
    
else:
    print("the student is not eligible for placement:")


````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#Q4

#WAP to accepet 5 nuumber in 5 different var and check maximum vlue and print using simple if
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
c=int(input("enter the 3rd number:"))
d=int(input("enter the 4th number:"))
e=int(input("enter the 5th number:"))

# if a>b and a>c and a>d and a>e:
#     print("a is the greatest number.")
# if b>a and b>c and b>d and b>e:
#     print("b is the greatest number.")
# if c>a and c>b and c>d and c>e:
#     print("c is the greatest number.")
# if d>b and d>c and d>a and d>e:
#     print("d is the greatest number.")
# if e>b and e>c and e>d and e>a:
#     print("e is the greatest number.")

````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

#Q5

#nested if else syntax:
#WAP acccept three number and check maximum number and print

n1 = int(input("enter first no."))
n2 = int(input("enter second no."))
n3 = int(input("enter third no."))

if n1>n2:
    if n1>n3:
        print("n1 is maximun number.")
    else:
        print("n3 is max")
else:
    if n2>n3:
        print("n2 is max")
    else:
        print("n3 is max")

#WAP for else if ladder

# if condition:
#     #statement
# elif condition:
#     #statement
# elif condition:
#     statement
# else:
#     default block


````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


#Q6

#WAP to if percentage is grater then 90 so addign grade A if percentage greater then 80 assign grade 'B' and if percentage is greater then 60 so assign grade C and if percentage is below 60 so print "FAIL"

physics =int(input("enter the marks physics: "))
chemistry = int(input("enter the marks chemistry:"))
maths = int(input("enter the marks of maths :"))

total= physics+chemistry+maths
percentage = total/3.0
print("total =",total)
print("percentage=",percentage)

if percentage>=90:
    print("grade A")
elif percentage>=80:
    print("Grade B.")
elif percentage>=60:
    print("Grade C.")
else:
    print("FAIL")

````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


#Q7

amount =int(input("enter the amount:"))
balance =500

if amount<= balance:
    print("transition successful.")
else:
    print("transition failed.")

````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


#Q8
name= "krishna"
#indexing = 012345678910
print(name[0])
print(name[1])
print(name[-1])
print(name[15])
print(name[0:5])
print(name[1:])
print(name[:5])
print(name[:])

````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


#Q9

S ="help4code is a best platfrom for practicing programming "
print(S.find("help4code"))
print(S.find("python"))
print(S.find("programming"))

````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


#Q10

# S = "harshal", "harish" , "kroshna"
# m = '|'.join(S)
# print(m)

S = "pyhton is a high level programming language"
print(S.lower())
print(S.upper())
print(S.swapcase())
print(S.title())
print(S.capitalize())

````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


#Q11

print=('Subject  Marks:')
phy=50
chem=60
math=70
print("physics={} chemistry={} Math={}".format(phy,chem,math))
print("physics={0} chemistry={1} Math={2}".format(phy,chem,math))
print("physics={X} chemistry={y} Math={z}".format(X=phy,y=chem,z=math))
total = phy+chem+math
print("Total Marks ",f"{total}")
print("Roll No=","7".zfill(4))

````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


#Q12

print('prashantjha777'.isalnum()) #True
print('prashantjha'.isalpha())
print('777f'.isdigit())
print('sdsdsdsd'.islower())
print(''.islower())
print('PRASHANTj'.isupper())
print('My Name Is Prashant'.istitle())
print(''.istitle())
print(''.isspace())
print("Hello".startswith("He"))
print("Hello".endswith("lo"))

````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


#Q13

import datetime
#datetime formatting
date=datetime.datetime.now()
print("It's now:{:%d/%m/%Y %H:%M:%S}".format(date))
