#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1.Palindrome using for loop


# In[ ]:


pal_num=input("Enter a number to check palindrome or not :- ")
check = ""
for i in range(len(pal_num)-1,-1,-1):
        check += pal_num[i]
if(check == pal_num):
    print("Its a palindrome number")
else:
    print("It is not a palindrome number")


# In[ ]:


2. Take a input from user and check how many vowels are there


# In[ ]:


vow = input("Enter a string : - ")
count = 0
for i in range(0,len(vow)):
    if(vow[i] ==  "a" or vow[i] ==  "e" or  vow[i] ==  "i" or vow[i] ==  "o" or vow[i] ==  "u"):
        count+=1
print("there are",count,"vowels in this string")


# In[ ]:


3. Take a input from user and check how many individual vowels are there


# In[ ]:


vow = input("Enter a string : - ")
a=e=i=o=u=0
for index in range(0,len(vow)):
    if(vow[index] ==  "a"):
        a+=1
    elif(vow[index] ==  "e"):
        e+=1
    elif(vow[index] ==  "i"):
        i+=1
    elif(vow[index] ==  "o"):
        o+=1
    elif(vow[index] ==  "u"):
        u+=1
print("a=",a,"\ne=",e,"\ni=",i,"\no=",o,"\nu=",u)


# In[ ]:


4.Take a inut from user whereever a vowel come so ,replace it with


# In[ ]:


vow = input("Enter a string : - ")
for i in range(0,len(vow)):
    if(vow[i] ==  "a" or vow[i] ==  "e" or  vow[i] ==  "i" or vow[i] ==  "o" or vow[i] ==  "u"):
        vow= vow.replace(vow[i],"#")

print(vow)


# In[ ]:


take a input from a user , if a string a str data type then get all the unique words from the string


# In[ ]:


string= input("Enter a string : - ")
word = string.split(" ")
print(*word , sep="\n")

