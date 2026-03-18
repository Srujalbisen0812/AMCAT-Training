Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Day7
#input = Srujal*is*a*good*programmer
#output =****Srujal is a good programmer
name = "Srujal*is*a*good*programmer"
newname=''
val=''
for i in name:
    if i!='*':
        newname+=i
    else:
        val+=i
print(newname) 
print(str(val)+newname)  

-------------------------------------------------------------------------------------------------------------------------------------
... 
... mylist=[]
... N=int(input("Enter the number of elements in the list: "))
... for i in range(N):
...     val=int(input("Enter the element: "))
...     mylist.append(val)
... for j in range(len(mylist)):
...     if j+1 in range(len(mylist)):
...         sum=mylist[j]-mylist[j+1]
... print("The sum of adjacent elements is: ",sum)
...    
... -----------------------------------------------------------------------------------------------------------------------------------
... 
... L=int(input())
... N=int(input())
... for _ in range(N):
...     W,H=map(int,input().split())
... 
...     if W<L or H<L:
...         print("UPLOAD ANOTHER") #HackerEarth Problem  "Roy and Profile Picture"
...     elif W==H:
...         print("ACCEPTED")
...     else:
...         print("CROP IT")
... 
... -----------------------------------------------------------------------------------------------------------------------------------
... 
... 
... list=[3,2,3,8,7,6,3,4]
... max=0
... for i in list:
...     if i>max:
...         max=i
... print(max)
... ----------------------------------------------------------------------------------------------------------------------------------------
...      
