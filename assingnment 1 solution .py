#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Q1##


# In[2]:


a="hemant"


# In[3]:


type(a)


# In[4]:


l=[4,5,8,"pwskills", 5456.5]


# In[5]:


type(l)


# In[6]:


f=32.564


# In[7]:


type(f)


# In[8]:


t = 1,5,3


# In[9]:


type(t)


# In[10]:


t1=(1,2,3,7,8)


# In[11]:


type(t1)


# In[12]:


##########################################


# In[13]:


##Q2##


# In[14]:


#(i)data type of var1  is string
#(ii) data type of var2  is string
#(iii) data type of var3  is list
#(iv) data type of var4  is  float


# In[15]:


###############################


# In[16]:


### Q3 ##


# In[17]:


# (i)  /  use for division 
# (ii)  %  use for modulo operation
#(iii) // use for floor division (rounds down to the nearest whole number)
# (iv) **  use for power operation ( exponentiation)


# In[18]:


###############################


# In[19]:


## Q4 ##


# In[20]:


l=[1 , 2 , 2.3 , "hemant", [1,8,90], (1,4,8) , True, {65,89}, {}, 5+8j ]


# In[21]:


for i in l:
    print(i)
    print(type(i))


# In[22]:


#######################################


# In[23]:


### Q5 ##


# In[24]:


A=30
B=5
i=1
while(i<=A):
    if i%B==0:
        print(i, "is divisible by ", B)
        print(i/B, "times")
    else:
         print(i, "is not divisible by ", B)
    i=i+1
    
 
        


# In[25]:


## Q6 ##


# In[26]:


l=list(range(26))


# In[27]:


l


# In[28]:


for i in l :
    if i%3==0:
        print(i, "is divisible by ", 3)
    else:
         print(i, "is not divisible by ", 3)
        


# In[29]:


### Q7## 


# In[30]:


# mutable objects can be changed after it is created
# immutable objects can not be changed after it is created


# In[31]:


l=[1,5,8,9] # list   # mutable 


# In[32]:


l[1]=22


# In[33]:


l


# In[34]:


a="hemant"  # string  # immutable


# In[35]:


a[2]


# In[36]:


a[2]="b"


# In[ ]:


a


# In[ ]:




