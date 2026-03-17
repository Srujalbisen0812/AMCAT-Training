Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> day 6
... Tuple : Tuple is exactly as similar as list datatype only the difference is that list is mutable but tuple is immutable that means we can not change the value.
... 
... ------------------------------------------------------------------------------------------------------------------------------------------
... def func(value,values):
...     var =1
...     values[0]=44
... t=3                                   #output - 3 44
... v=[1,2,3]
... func(t,v)
... print(t,v[0])    
... 
... ------------------------------------------------------------------------------------------------------------------------------------------
... 
... 
... def f(i, values=[]):
...     values.append(i)
...     print(values)
... f(1)
... f(2)
... f(3)
... 
... -------------------------------------------------------------------------------------------------------------------------------------------
... 
... fruit_list1=['Apple','Berry','Cherry','Papaya']
... fruit_list2=fruit_list1
... fruit_list3=fruit_list1[:]
... fruit_list2[0]='Guava'
... fruit_list3[1]='kiwi'
... 
... sum=0
... for ls in (fruit_list1,fruit_list2,fruit_list3):
...     if ls[0]=='Guava':
        sum+=1
    if ls[1]=='kiwi':
       sum+=20
print(sum)       

-----------------------------------------------------------------------------------------------------------------------------------------



list=[7,3,9,2,8]
list.sort()
print(list)  #output [2, 3, 7, 8, 9]  8
print(list[-2])

----------------------------------------------------------------------------------------------------------------------------------------

Set Datatype:=

if we don’t want duplicate value and we want to represent random data that means there is no order wise data required then we should go for set datatype.

➤ No Order wise data (random)
➤ Heterogeneous data are possible in set
➤ set represented by {} parenthesis
➤ Duplicate data are not allowed
➤ set by nature it is growable
➤ It is mutable .


myset={1,2,"sanjay",5.66,"rahul","ayush","ramesh","ankit","rishikesh"}
print(myset)

myset.discard(3)
print(myset)

----------------------------------------------------------------------------------------------------------------------------------------

list=[0,1,0,3,12]

for i in list:
    if i==0:
        list.remove(i)
        list.append(i)
print(list)        

----------------------------------------------------------------------------------------------------------------------------------------


A=[1, 2, 3]
B=[2, 3, 4]
C=[3, 4, 5]
for i in A:
    if i in B and i in C:
        print(i)
--------------------------------------------------------------------------------------------------------------------------------------

Time Coversion HACKERRANK

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    

    period = s[-2:]
    time = s[:-2]
    
    hours, minutes, seconds = time.split(":")
    
    if period == "AM":
        if hours == "12":
            hours = "00"
    else:
        if hours != "12":
            hours = str(int(hours) + 12)
    
    return f"{hours}:{minutes}:{seconds}"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()


