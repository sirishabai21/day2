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
