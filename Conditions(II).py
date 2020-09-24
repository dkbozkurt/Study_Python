#!/usr/bin/env python
# coding: utf-8

# # Conditions

# and(1 1 true) , or (0 0 false) , not (degil)

# In[1]:


5<10 and 3<8


# In[2]:


5>10 and 3>8


# In[3]:


5<10 and 3>8


# In[4]:


5<10 or 3<8


# In[5]:


5>10 or 3<8


# In[6]:


5>10 or 3>8


# In[7]:


not 5>3


# In[8]:


not 5<3


# ### Ownership operators

# in , not in

# In[1]:


b= [3,5,7,8]


# In[2]:


3 in b


# In[3]:


6 in b


# In[4]:


5 not in b


# ### Assignment operators

# In[18]:


a =4


# In[19]:


a=a+5
a


# In[20]:


a+=5
a


# In[21]:


a-= 5
a


# In[22]:


a*=10
a


# In[23]:


a/=10
int(a)


# In[24]:


a//=2#kalanı umursamadan bölüm yapan operatör ( // ) (a=a // 2)


# In[25]:


a


# In[26]:


a%=3
a


# ### IF and ELSE

# In[28]:


if 5>3:
    print("5 is greater than 3.")
else:
    print("Wrong!")


# In[31]:


id_name=input("ID : ")
password=input("Password : ")

if id_name=="dogukankaan" and password=="1998":
    print("Access Granted!")        
else:
    print("Wrong ID or password!")


# ### ELIF

# In[34]:


id_name=input("ID : ")
password=input("Password : ")

if id_name=="dogukankaan" and password=="1998":
    print("Access Granted!")     
elif id_name!= "dogukankaan":
    print("Wrong ID!")
else:
    print("Wrong password!")


# In[39]:


grade=int(input("Enter your mark : "))

if grade >= 90 and grade <=100:
    print("AA !")
elif grade >= 75 and grade <90:
    print("BB !")
elif grade >= 60 and grade <75:
    print("CC !")
elif grade >= 50 and grade <60:
    print("DD !")
elif grade <50:
    print("FF !")
else:
    print("Wrong mark value!")


# ## NOTE

# If else durumu şu sekildede yazılabilir;

# In[41]:


print("5 is greater than 3") if 5>3 else print("Wrong!") 
# if ten önceki ifade dogru olma durumu yanlıs ifade ise elseden sonrakı durum.


# ### Nested IF

# In[43]:


num=int(input("Enter an number: "))

if num>=0:
    if num==0:
        print("Number is zero!")
    else:
        print("Number is positive!")
else:
    print("Number is negative")


# ## NOTE

# Eğer bir fonks(if elif else...) ifadesinin içeriğini daha sonradan yazıcaksak yada düzenliceksek, pass programın o satırı atlamasını saglayabiliriz. 

# In[44]:


if 3>1:
    pass


# In[45]:


#Doğukan Kaan Bozkurt

