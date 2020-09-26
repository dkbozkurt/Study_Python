#!/usr/bin/env python
# coding: utf-8

# ### WHILE

# In[6]:


x=5

while x>3:
    print("x is greater than 3")
    x-=1
else:
    print("x is equals to 3")


# ##### break & continue

# In[8]:


x=0

while x<10:
    print("x=",x)
    if x==5:
        break
    x+=1
    
else:
    print("X is equals to 10.")


# In[11]:


x=0

while x<10:    
    x+=1
    if x==5:
        continue ## fonksyonun başına geri döner.
    print("x=",x)
    
else:
    print("X is greater than 10.")


# ### For

# In[12]:


numbers = [1,2,3,4,5,6,7,8,9]


# In[14]:


for num in numbers:
    print("Number =",num)
else:
    print("Loop has finished")


# In[15]:


for num in numbers:
    print("Number =",num)
    if num==5:
        break #for döngüsünden direkt çıkar
else:
    print("Loop has finished")


# In[16]:


new=[1,2,3]


# In[19]:


for num in numbers:
    for new_num in new:
        print("Number =",new_num)
else:
    print("Loop has finished")


# In[20]:


for i in range(1,20): #range(x,y,t) x den y ye kadar t artarak.
    print(i)


# In[21]:


list(range(5,20,2))


# In[22]:


for i in range(1,20):
    pass #buraya daha sonra bir şeyler ekleyebeilirim.


# ##### Examples of For loops

# In[23]:


colors= ["red","yellow","orange","green","blue","purple"]


# In[26]:


for i in colors:
    print(i)


# In[46]:


salary = [2000,3000,4000,5000,6000,7000]


# In[50]:


for i in range(0,5):
    print(salary[i]*2)


# #### Doğukan Kaan Bozkurt
