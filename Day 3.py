Q1 for i in range(5):
    print(i)



Q2 for i in range(1,10,2):
    print(i)


Q3 for i in range(1,11):
    print(i*2)


Q4 for i in range(1,11):
    print(i*2," ",i*3," ",i*4)

print()

Q5for i in range(1,11):
    print(i*11," ",i*12," ",i*13)


Q6 name ='prasahat'
data = ['a', 'e', 'i', 'o', 'u']
vo++wels = 0
cons = 0
for i in name:
    if i in data:
        vowels += 1
    else:
        cons += 1
print('vowels:', vowels)
print('consonants:', cons)




Q6 name ='prasahat'
data = ['a', 'e', 'i', 'o', 'u']
for i in name:
    if i not in newname:
        newname += i
print(name)
print(newname)


Q7 a=50
b=30
c=20
d=10
print((a+b)*(c/d))
print((a-b)*(c/d))


x=['A','B','C']
y=['A','B','C']
Z=[1,2,3,4]
print(x==y)



Q7 mylist = [2,5,8,4,1,9,8]
even = []
odd = []
for num in mylist:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print('Even numbers:', even)
print('Odd numbers:', odd)



mylist = [2,5,8,4,1,9,8]
even = []
odd = []
for num in mylist:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print('Even numbers:', even)
print('Odd numbers:', odd)
total_sum = sum(mylist)
print('Sum of all numbers:', total_sum)


val=[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(val.index(1))
print(val.index(2))
print(val.index(3))
print(val.index(4))
print(val.index(5))
print(val.index(6))



n=[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))
print(n.count(5))
print(n.count(6))



rollno =[3,5,7,9,11,4,5,2]
for x in rollno:
    if x==2 or x==4 or x==6 or x==8 or x==10:
        print("even no is found",x)
        break



for i in range(10) :
    if i==5:
        continue
    print(i)



ch =ord(input("Enter a single character: ")
if ch >= 65 and ch <= 91:
      print("The character is an uppercase letter.")
elif ch >= 97 and ch <= 122:   
    print("The character is a lowercase letter.")
elif ch >= 48 and ch <= 57:
    print("The character is a digit.")
else:
    print("The character is a special character."))








v=['a','e','i','o','u']
w=input("Enter a single character: ")
found=[]#a
for i in v:
    if i not in found:
        found.append(i)
    print('found a vowel=',found)
    print('Unique vowels', len(found),'from the given input=',w) 
