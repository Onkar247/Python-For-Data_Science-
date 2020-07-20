
# coding: utf-8

# In[7]:

#p1
n=int(input("enter the limit="))
s=dict()
for i in range(1,n+1):
    s[i]=x**3
print(s) 


# In[16]:

#p4
import random
for x in range(10):
    print(random.randrange(10, 100, 2), end=' ')


# In[18]:

#p3
lower = 1
upper = 100


print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[19]:

#p2
str = input("Enter a comma seprated string : ")

if len(str)>0:
    sstr=""
    wordList = str.split(",")
    wordList = sorted(wordList)
    for w in wordList:
        sstr +=w
        sstr +=","
    sstr = sstr[:-1]
    print("Sorted String : ",sstr)
else:
    print("String is empty.")


# In[20]:

#p5
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


# In[ ]:



