#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input("Enter number of digits you want in series:"))
a=0
b=1
print("\n Fibonacci numbers are:")
print(a,",",b,end=",")
for i in range(2,n):
    c=a+b
    print(c,end=",")
    a=b
    b=c


# In[ ]:




