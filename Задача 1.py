#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = list(input("num = "))
if x.count('6')>0:
    x.insert(x.index('6'), '9')
    x.remove('6')
print("".join(str(i) for i in x)) 


# In[3]:


def twist (A):
    x = list(A)
    if x.count('6')>0:
        x.insert(x.index('6'), '9')
        x.remove('6')
    print("".join(str(i) for i in x))


# In[4]:


twist ("9669")
twist ("9996")
twist ("9999")

