Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def msg():#called function
    val1 = int(input("Enter first value:"))
    val2 = int(input("Enter second value:"))
    print(val1+val2)
msg()#calling function
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def msg():#called function
    val1 = int(input("Enter first value:"))
    val2 = int(input("Enter second value:"))
    print(val1+val2)
res=msg()#calling function
print("result is",res)    

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def msg():#called function
    val1 = int(input("Enter first value:"))
    val2 = int(input("Enter second value:"))
    sum=val1+val2
    mul =val1*val2
    sub=val1-val2
    div=val1/val2
    return sum, mul, sub, div

res=msg()#calling function
print("result is",res)    

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Types of argument
1.Positional Argument
2.Keyborad Argument
3.Default Argument
4.Variable length argument/variable number of argument
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def personalInfo(fname, lname):
    print(f"First Name: {fname}")
    print(f"Last Name: {lname}") # Positional Argument
personalInfo("Lawrence", "Bishnoi")   


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def personalInfo(fname, lname):
    print(f"First Name: {fname}")  #Keyborad Argument
    print(f"Last Name: {lname}")
fname ="Lawrence"
lname = "Bishnoi"    
personalInfo("Lawrence", "Bishnoi")    
     
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def cityName(city="Nagpur"):
    print("City Name",city)
cityName("Mumbai")
cityName("Pune") #Default Argument
cityName()

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def cityName(city="Nagpur"):
    print("City Name",city)
cityName("Mumbai","Ngapur","Delhi")
cityName()

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "123":
        print("Login successful!")
    else:
        print("Login failed. Please try again.")    
login()        

OutPut
PS D:\Amcat> python -u "d:\Amcat\day5.py"
Enter your username: admin
Enter your password: 123
Login successful!

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


myList =[4,2,7,8,5,4,1]
def searchValue(traget):
    for i in range(len(myList)):
        print (myList[i])
traget=7
searchValue(traget)                

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def searchValue(traget):
    for i in range(len(myList)):
        if myList[i] == traget:
            return i
        
    return -1
myList =[4,2,7,8,5,4,1]
traget=10
res = searchValue(traget)
if res != -1:
    print(f"Value found at index number {res}")
else:    
    print("Value not found")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def searchValue(traget):
    sum=0
    for i in range(len(mylist)):
        sum = sum + mylist[i]
    return sum
mylist = [1,2,3,4,5]
res = searchValue(mylist)
print("sum of list is", res)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    sum=0
    for i in range(len(ar)):
        sum= sum+arr[i]
    return sum
if  __name__=='__main__'        

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
... #
... # The function is expected to return an INTEGER_ARRAY.
... # The function accepts following parameters:
... #  1. INTEGER_ARRAY a
... #  2. INTEGER_ARRAY b
... #
... 
... def compareTriplets(a, b):
...     alice=0
...     bob=0
...     for i,j in zip(range(len(a)), range(len(b))):
...         if a[i] > b[j]:
...             alice +=1
...         if a[i] < b[j]:
...             bob +=1
...         if a[i]==b[j]:   
...             pass   
...     return alice,bob  
... if __name__ == '__main__':
...     fptr = open(os.environ['OUTPUT_PATH'], 'w')
... 
...     a = list(map(int, input().rstrip().split()))
... 
...     b = list(map(int, input().rstrip().split()))
... 
...     result = compareTriplets(a, b)
... 
...     fptr.write(' '.join(map(str, result)))
...     fptr.write('\n')
...     fptr.close()
... 
... 
... ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
... 
...    sum=0
...     for i in range(len(ar)):
...         sum+=ar[i]
...     return sum             
... 
... 
...     
... 
... 
... 
...     
...     
