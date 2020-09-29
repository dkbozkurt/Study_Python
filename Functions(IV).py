#!/usr/bin/env python
# coding: utf-8

# # Functions

# In[3]:


def get_square(x):   #def func(x) yazarak fonks yazabiliyoruz.
    print(x**2)
    
get_square(5)
get_square(10)


# In[4]:


def area(r):
    pi=3.14
    print(pi*r**2)
    
area(6)


# ##### sep , end
# 
# Default--> sep="" , end="\n"

# In[8]:


print("Doğukan","Kaan","Bozkurt",sep="/",end=".") 
#Burada sep parametresi seperator anlamına gelir.Elemanları seperator ile istenen karakterle ayırabiliriz.
#end ise satır bittiğinde yapmak istediğimizi yada basmak istediğimizi yazabiliriz.


# In[10]:


print("Doğukan","Kaan","Bozkurt",sep="\n",end=";") 


# In[13]:


area1=area(6)
area2=area(8)


# In[15]:


area_total=area1+area2 #Burada hata alırız bu nedenle return kullanmalıyız.


# ##### return
# 
# Fonksiyonun değeri olarak atamış oluruz. Fonksiyonlarda returnu kullanıp ilerle print yerine.

# In[16]:


def area(r,pi=3.14):
    return pi*r**2


# In[17]:


area1=area(6)
area2=area(8)


# In[19]:


area_total=area1+area2
area_total


# In[20]:


def asdasdasd():
    pass


# In[21]:


def even(x):
    if x%2==0:
        print("X is an even number.")
    else:
        print("X is an odd number.")


# In[25]:


ev=even(4)
even(5)


# In[27]:


type(ev) 
#Bunun nedeni printle bir çıktı aldık bu yüzden nonetype verir.Fakat returnle yaparsak ozaman str alırız.


# In[32]:


def even(x):
    if x%2==0:
        return "X is an even number."
    else:
        return "X is an odd number."


# In[34]:


ev=even(4)
ev


# In[36]:


type(ev) # Returnle dönme sonucunda ev'in tipi string oldu.


# ##### Note:
# 
# Shift + Taba basarak gömülü fonk. özelliklerini ve alabileceklerini görebiliriz.

# In[38]:


help(print) #Ayrıca help kullanarakta ulaşabilriz.


# ##### Note:
# 
# Default olarak fonk içindeki bir elemena atama yapmak için fonks tanımlarken parantez içinde değeri eşitlik değeri yazılır.

# In[51]:


def id(name="Empty",surname="Empty",age="Empty",num="Empty"):
    print("Name: ",name,"\nSurname: ",surname,"\nAge: ",age,"\nID Number: ",num)


# In[53]:


id("Doğukan Kaan","Bozkurt",22)


# In[56]:


id(22,99999999999) #eğer age ve num atamassak sirasiyla attigi icin hata olusur.


# In[57]:


id(age=22,num=99999999999)


# # *args and *kwargs

# *args and *kwargs allow you pass multiple arguments or keywords arguments to a function.

# ### Arbitrary Arguments, *args
# 
# -İçerisine ne kadar değer girileceğini bilmediğimiz durumlarda kullanılır.
# 

# # *args yerine Tuples girdisi alır.

# In[59]:


def add(x,y,z):
    return x+y+z


# In[60]:


add (3,4,5)


# In[68]:


def add(*args): #Ne kadar girilse girilsin demek, istediğimiz kadar sayıyı yazıp toplayabiliyoryuz.
    addition=0
    for i in args:
        addition+=i
    print(addition)


# In[69]:


add(1,2,3,4,5,6,7,8,9,10)


# ##### Note:
# 
# Asil önemli olan şey * , args yazmasakta olur. Ama diğer kod yazanların okumasındaki temizlik için args kullanılır.

# In[74]:


def name(*args):
    print("{} {} {} Öğrenci".format(args[0],args[1],args[2]))
#Buradaki gibi de önceden belirlenen boşluk sayısı kadar girdi alınabilir. .format kullanımayi unutmamak gerekli.


# In[75]:


name("Doğukan","Kaan","Bozkurt")


# ### Arbitrary Keyword Arguments, **kwargs

# ** kwargs works just like *args, but instead of accepting positional arguments it accepts keyword (or named) arguments
# 
# If you do not know how mant keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definiton.
# 
# This wayy the function will receive a dictionary of argumets,and can access the items accordingly.

# # **kwargs yerine Dictionary girdisi alır

# In[79]:


def id_inf(**kwargs):
    print("kwargs:",kwargs)


# In[80]:


id_inf(name="Doğukan Kaan",surname="Bozkurt")


# In[87]:


def id_inf(**kwargs):
    for key,value in kwargs.items():
        print("{} = {}".format(key,value))


# In[89]:


id_inf(name="Doğukan Kaan",surname="Bozkurt",age="22",email="dkaanbozkurt@gmail.com")


# In[91]:


def new(*args,**kwargs):
    print("args:",args,"kwargs",kwargs)


# In[94]:


new(1,2,3,4,5,6,name="Doğukan Kaan",surname="Bozkurt") #Burada da tuple ve dic olarak farkını kendisi alıyor otomatik.


# ##### Note:
# 
# Sıralama da args önce verildiyse önce tüm argslar girilir. Sıralamada hata varsa kod hata verir.**Sıralamaya dikkat**

# In[96]:


new(1,2,3,4,5,6,name="Doğukan Kaan",surname="Bozkurt",7,8,9) # Burada hata verme nedeni args kwargs,args diye gitmesi


# In[100]:


def combine(**kwargs):
    end=""
    for keyy in kwargs.values():
        end=end+keyy
    return end


# In[103]:


combine(a="Python ",b="is ",c="the ",d="best ",e="programming ",f="language.")


# # Python Global and Local variables

# ### Global Variables

# In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a globa variable can be accessed inside or outside of the function.

# In[1]:


x=10

print(x)


# ### Local Variables

# A variable declared inside the function's body or in the local scope is known as local variable.

# In[6]:


x=10 #Bu global variable olarak tanımlanır. O yüzden func. dışıdaki çıktıda 10 basar.

def function(): #funcların içinde tanımlanan değerler local variabledir.
    x=5
    print(x)
    
print(x)


# In[7]:


function()


# ### Python Lambda Function

# A lambda func is a small anonyumous funch.
# 
# A lambda func can take any number of arguments, but can only have one expression.
# 
# Use lambda when you use one time this func.
# 
# lambda arguments: expression

# In[3]:


def kare(x):
    return x**2 #Bu func. lambda func çevirmek için gelecek satirlar izlenmeli.


# In[4]:


kare(8)


# In[5]:


x=lambda x:x**2


# In[6]:


x(10)


# Why Use Lambda Func?
# 
# The power of lambda is better shown when you use them as an anonymous func. inside another func.

# The filter() func is Python takes is a func. and a list as arguments. The filter() func returns an iterator were the items are filtered through a func. to test if the item is accepted or not.
# 
# The func. is called with all the items in the list and a new list is returned which contains items for which the func. evaluates to True.
# 
# Here is an example use of filter() func. to filter out onlt even numbers from a list.

# In[8]:


x=[1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x:(x%2==0),x))


# #### Map()

# Example use with map()
# 
# The map() function in Python takes in a function and a list.The map() func. executes a specified func for each item in a iterable.The item is sent to the func. as a parameter.
# 
# The func. is called with all the items in the list and a new list is returned which contains items returned by that func. for each item.
# 
# Here is an example use of map() func. t odouble all the items in a list.

# In[24]:


x=[1,2,3,4,5,6,7,8,9,10]

y=list(map(lambda x:x**2,x))#list(map(lambda x(1):x**2,x(2)) 
#Burada her bir x(1) değeri için x**2 ,işlemini uygulayıp x(2) nin o indeksine eşitleyip bas fakat x in içeriğini değiştirme.


# ## Note:
# 
# filter() filtereden geçirip belirli çıktılar almamızı sağlarken map() tüm elemanlar üzerine işlem uygulama ve ona göre cıktı almamızı saglar.
# 

# In[26]:


print(x)
print(y)


# ### Some Built-in Functions(Gömülü Fonksiyonlar)

# abs() Returns the absolute value of a number

# In[27]:


abs(-7.50)


# bin() Returns the binary version of a number

# In[28]:


bin(4)


# enumerate() Takes a collection (e.g. a tuple) and returns it as an enumerate object

# In[29]:


colors=["red","orange","yellow","green","blue","purple"]


# In[30]:


xyz=enumerate(colors)


# In[32]:


list(xyz)


# In[33]:


for index,colors in enumerate(colors):
    print(index,colors)


# max() Returns the largest item in an iterable.(iterable = tekrarlanabilir)
# 
# The max() func. returns the item with the highest value, or the item with the highest value in an iterable
# 
# If the values are strings, an alphabetically comparison is done.

# In[34]:


kkk=[2,3,7,4,12,35]
max(kkk)


# In[36]:


trtrtr=["d","o","g","u","k","a","n"]
max(trtrtr) #alfabedeki son sıradaki harf.


# min() returns the smallest item in an iterable 
# 
# The min() func. returns the item with the lowest value, or the item with the lowest value in an iterable
# 
# If the values are strings, an alphabetically comparison is done.

# In[37]:


kkk=[2,3,7,4,12,35]
min(kkk)


# In[38]:


trtrtr=["d","o","g","u","k","a","n"]
min(trtrtr) #alfabedeki ilk sıradaki harf.


# pow() Returns the value of x to the power of y
# 
# The pov() func. returns the value of x to the power of y (xy).
# 
# If a third parameter is present, it returns x to the power of y, modulus z.
# Return the value fo 5 to the power of 4,modulus 10 (same as(5 * 5 * 5 * 5) % 10)

# In[40]:


pow(2,5)


# In[41]:


pow(5,4,10)


# reversed() Returns a reversed iterator

# In[44]:


kk=[2,3,7,40,12,35,5]
y=reversed(kk)
list(y)


# round() Rounds a numbers

# In[47]:


round(3.14567,4) #round(x,y) x sayısını yuvarladiginda , den sonra y kadar sayi görürüz.


# sorted() Returns a sorted list

# In[48]:


kk=[2,3,7,40,12,35,5]
sorted(kk)


# In[50]:


sorted(kk,reverse= True) # büyükten küçüğe sıralamak için.


# sum() Sums the items of an iterator

# In[51]:


kk=[2,3,7,40,12,35,5]


# In[53]:


sum(kk)


# zip() Returns an iterator, from two or more iterators

# In[54]:


za=[1,2,3,4]
colors=["red","orange","yellow","green","blue","purple"]


# In[56]:


list(zip(za,colors))


# In[57]:


#Doğukan Kaan Bozkurt

