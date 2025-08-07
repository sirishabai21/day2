name = "sirisha"
name = "s"+"irisha"
print(name)

# to get all first letters upper
str1="All silver tea cups." 
for i in range(len(str1)):
    if str1[i]==" " and str1[i+1]!=" ":
        str1=str1[:i+1]+str1[i+1].upper()+str1[i+2:]
print(str1)

#another method
str1="All silver tea cups."
str2=str1.split()
print(str2)    

#another method
str1="All silver tea cups."
str2=str1.title()
print(str2)

#another method
str1=input().title()
print(str1) 

#pascal case
str1="All silver tea cups".title()
str2=str1.split(" ")
str3="".join(str2)
print(str3)

#snake case
str1="All silver tea cups".lower()
str2=str1.split(" ")
str3="_".join(str2)
print(str3)

#camel case
str1="All silver tea cups".title()
str2=str1.split(" ")
str3="".join(str2)
str3=str3[0].lower()+str3[1:]
print(str3)
  
str1="All silver tea cups".title()
str2=str1.split(" ")
str3="-".join(str2)
print(str3)

#for vowel count
str1="all silver tea cups".lower()
count=0
for i in str1:
    if i in "aeiou":
        count+=1
print(count)

#pascal case
str1="All silver tea cups".title()
str2=str1.split(" ")
str3="".join(str2)
print(str3)

#snake case
str1="All silver tea cups".lower()
str2=str1.split(" ")
str3="_".join(str2)
print(str3)

#to convert lower to upper and upper to lower
n = input()
new_str =" "
for i in n:
    if i.isupper():
        new_str += i.lower()
    else:
        new_str += i.upper()
print(new_str)

# to add list
li=[1,2]
li2=[3]
res = li+li2+["rtt"]+[True,6789.8]
print(res)

# to find largest number
l1 = input()
l2 = sorted(l1)
print(l2[len(l2)-1])

#another method
list_1 = [3,6,5,7,9,8]
print(max(list_1))

#another method
list_1 = [3,6,5,7,9,8]
highest = list_1[0]
for i in range(len(list_1)):
    if list_1[i]>highest:
        highest = list_1[i]
print(highest)

#to find second largest
l1= input()
l2 = sorted(l1)
print(l2[len(l2)-2])

# list_1 = [3,6,5,7,9,8]
second = list_1[0]
for i in range(len(list_1)):
    if list_1[i]>second and highest>list_1[i]:
        second = list_1[i]
print(second)

# to get only single without any duplicates
list_1 = [3,6,4,7,6,7,3]
list_2=set(list_1)
print(list_2)

# to print single unique number
list_1 = [3,6,5,4,5,6,3]
first_sum = sum(list_1)
second_sum = sum(set(list_1))*2
res = second_sum-first_sum
print(res)

# factorial of a nnumber
n=int(input("enter number"))
fact=1
for i in range(n,1,-1):
    fact *= i
print(fact)

#sum of first 10 multiples of given number
n=int(input())
sum=0
for i in range(1,11):
    sum+=n*i 
print(sum)

#another method
n=int(input())
print(n*55)

# linear search for target indexes
list_1 = [1,7,9,7,4,6,2]
target = 7
for i in range(len(list_1)):
    if target==list_1[i]:
        print(i)
        break
 
# binary search for targeting index
list_1 = [1,2,3,4,5,6,7,8,9,10]
target = 7
start = 0
end=len(list_1)-1
index=-1
while(start<=end):
    middle=(start+end)//2
    if list_1[middle]==target:
        index = (middle)
        break
    elif list_1[middle]>target:
        end = middle-1
    elif list_1[middle]<target:
        start=middle+1
print(index)
 
# # to print in increasing order       
n=int(input())
for i in range(1,n+1):
    print("* "*i)

# to print in decreasing order
n=int(input())
for i in range(n,0,-1):
   print("* "*i)

#n=int(input())
for i in range(1,n+1):
    str1=""
    for j in range(1,i+1):
        str1+=str(j)+" "
    print(str1) 

# to print numbers in decreasing order
n=int(input())
for i in range(n,0,-1):
    str1=""
    for j in range(1,i+1):
        str1+=str(j)+" "
    print(str1)

# to get pyramid
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i) +"* "*i)    

# to get reverse pyramid
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i) +"* "*i)

# to get hallow pyramid
n=int(input())
for i in range(1,n+1):
    if i == 1 or i == n:
        print("* "*i)
    else:
        print("*"+" "*(2*i-3)+"*")
