#!/usr/bin/env python
# coding: utf-8

# # Data types and variables(I)

# #### Best way to learn a programming language is to use it.

# Doğukan Kaan bozkurt

# ### Print() - input()

# In[1]:


print("Dogukan Kaan Bozkurt")


# In[3]:


input("What is your name?")


# ### Variables and constants

# In[6]:


name= "Dogukan Kaan"
surname="Bozkurt"

print(name)
print(surname)


# In[8]:


PI= 3.14 #caps ile yazilirsa bu constant olarak tanimlanir. Daha sonra degistirilemez.


# In[11]:


name,surname=surname,name #Degiskenlerin yerlerini tek satirda degistirebildik.


# In[12]:


print(name)
print(surname)


# ### Data types - Numbers

#  Numbers - Sayilar ;
#  String - Karakter dizileri ;
#  Boolean - True & False ;
#  List - Listeler ;
#  Tuple - Demetler ;
#  Dictionary - Sözlükler ;
#  Set - Kumeler ;

# ### Numbers

# In[14]:


Age = 22


# In[15]:


5+5


# int - 542 ;
# float - 5.56 ;
# long - 51924361L ;
# complex - 3.14j ;

# In[16]:


5+5.68


# In[17]:


55/5 # bölüm tam çıksa bile float seklinde output verir.


# In[18]:


40%7


# In[19]:


4**3 #4 un kacinci ustu anlamına gelir.


# In[20]:


40//6 # Boluneni gosterir. Noktadan sonrasini siler yuvarlamaz!


# In[21]:


round(4.56) #round() yuvarlama islemini yapan fonksiyon


# ### Strings

# 'Dogukan';
# 
# "Dogukan";
# 
# """Dogukan""" eger string bir kac satirdan olusacaksa 3 tirnak kullanılir diger tirnaklar tek satir icin gecerlidir.

# In[39]:


name = "Dogukan Kaan Bozkurt"


# In[31]:


print(name[0])
print(name[7])
print(name[-2])


# In[54]:


print(name[0:7]) #7 dahil değildir.
print(name[0:7:2]) # 0 dan başlayıp 7 ye kadar ikişerli.


# In[9]:


#stringlerde tekli olarak değiştirilme yapılamaz. name[3]="c" gibi.


# In[32]:


exp= "Turkey\'s the largest city is Istanbul." 
# buradaki ' tek tırnakta string kapanmaması için kaçış dizisi olan (\)Back slash tırnaktan önce getirilir. ***********
print(exp)


# In[33]:


#C deki gibi \n ve \t alt satira geçme yada bosluk bırakmayaya yarıyor.
exp1= "Turkey\'s \nthe \tlargest city is \nIstanbul."
print(exp1)


# In[20]:


"Dogukan " * 3


# In[21]:


"Dogukan" + " Bozkurt"


# ##### Methods

# In[22]:


"dogukan kaan bozkurt".upper() #.upper() fonk stringin bütün harflerini büyütür.


# In[23]:


"DOGUKAN KAAN BOZKURT".lower() #.lover() fonk stringin bütün harflerini küçültür.


# In[24]:


"dogukan kaan bozkurt".capitalize() #.capitalize() fonk stringin baş harfini büyütür.


# In[29]:


name.count("D") #.count("a") stringinin içinde kaç tane "a" geçtiğini söyler


# In[34]:


name.find("Bozkurt") #d.find("Bozkurt"), stringin içinde bozkurtu bulup ilk harfinin index numarasını basar.


# In[40]:


name.index("k") #.d.index("k") string içindeki ilk k nin indexini verir.


# In[48]:


new="      Dogukan Kaan Bozkurt      "


# In[49]:


print(new.lstrip()) #d.lstrip() stringin solundaki boşluğu siler .rstrip() sağındakini. strip() ise iki yanındaki boşlugu siler.
print(new.rstrip())
print(new.strip())


# In[50]:


name.replace("Bozkurt","trukzoB") #d.replace("a","b") string içindeki a nın yerine b yi koyar.


# In[51]:


isim="Dogukan Kaan"
soyisim="BOZKURT"


# In[53]:


print("My name is {} and my surname is {}. ".format(isim,soyisim))
#d.format(a,b) print içinde {} ile bırakılmış alanlara formatin içindeki bilgilerle doldurur.


# ### Boolean

# Kısaca true false çıktısını veren veri tiplerine boolean denir.

# In[55]:


5 > 4


# In[56]:


7< 5


# In[58]:


5==5 # çift eşittir her zaman karşılaştırma için kullanılmalıdır. Yoksa eşitlik algılanır.


# In[59]:


6!=6


# ### Lists [ ]

# In[60]:


person= ["Dogukan Kaan","Bozkurt",22,"Python"]


# In[62]:


print(person)


# In[64]:


print(person[0])
print(person[0:3])


# In[65]:


person[0] = "Dogukan" # Listelerde değişiklik yapılabilir.


# In[66]:


person


# In[67]:


people = [["Dogukan Kaan","Bozkurt"],[175,22]]


# In[70]:


print(people[1][0])
print(people[0][1])


# In[71]:


len(people)


# ##### Methods

# In[1]:


sayilar=[1,1,4,5,8,9,5,64,8,8696,464]


# In[2]:


len(sayilar)


# In[4]:


sayilar[-7:-2:2]


# In[5]:


sayilar[:-2]


# In[6]:


sayilar.append(10000) #d.append(n) d lsitesine n nesnesini ekler.


# In[7]:


print(sayilar)


# In[8]:


sayilar.remove(64) #d.remove(n) d lsitesine n nesnesini çıkarır.
print(sayilar)


# In[9]:


sayilar.pop() #d.pop() d listesindeki son sayıyı çıkarır.
print(sayilar)


# In[10]:


sayilar.pop()


# In[11]:


sayilar


# In[12]:


sayilar.pop(4) #d.pop(i) d listesindeki i. indexteki sayıyı çıktı olarak basıp listeden cıkarır.


# In[13]:


sayilar


# In[15]:


yeni=sayilar.copy() #d.copy() listeyi kopyalama.
print(yeni)


# In[17]:


a=[1,2,3,4]
b=[5,6,7,8]
c=a+b
print(c)


# In[21]:


d=[1,2,3,4]
f=[5,6,7,8,9,10]
d.extend(f) #d.extend(f) d listesi ile f listesini birleştirip d ye atar.


# In[22]:


d


# In[30]:


z=[5,6,7,8,9,10,10,10]
z.count(10) #d.count(n) d listesinde n den kaç adet var oldugunu basar.


# In[31]:


z.index(6) #d.index(x) x elemanın kaç numaralı indexte oldugunu bastırır.


# In[32]:


z.insert(3,"odd") #d.insert(i,n) d listesinin i numaralı indexine  n objesini ekler ve kalanlar sağa kayar.


# In[33]:


z


# In[34]:


z.pop(3)


# In[35]:


z


# In[36]:


g=[3,5,2,88,23,67]
g.sort() #d.sort() listeyi küçükten büyüğe sıralar.


# In[37]:


g


# In[38]:


g.sort(reverse=True) #d.sort(reverse=True) listeyi büyükten küçüğe sıralar.


# In[39]:


g


# In[40]:


exp99=["dogukan","kaan","bozkurt"]
exp99.reverse() #d.reverse() listeyi ters çevirir.


# In[41]:


exp99


# In[42]:


exp99.sort()


# In[43]:


exp99


# In[46]:


exp99.sort(reverse=True) #Alfabe sırasına göre ters yazılmış şekline çevirecek.


# In[47]:


exp99


# In[48]:


exp99.clear() #d.clear() d listesinin içindeki elemanları temizler.
exp99


# ###  Dictionaries { }

# key : value
# 
# Sırasızdır.Index kullanılamaz.
# 
# Key'ler değiştirilemez. Value değerleri değiştirilebilir.

# In[49]:


id = { "name":"Dogukan",
      "surname":"Bozkurt",
      "idnum":99999999999,
      "from":"Kocaeli"
}


# In[51]:


id["name"]


# In[52]:


id["name"] = "kaan"


# In[53]:


id


# In[54]:


len(id)


# In[56]:


id["year"] = 1998
id


# In[58]:


id = { "name":"Dogukan",
      "surname":"Bozkurt",
      "idnum":99999999999,
      "from":"Kocaeli",
      "inf": {
          "email":"dkaanbozkurt@gmail.com",
          "Siblings":1,
      }
}

id


# In[61]:


# Key yerine sayı verilebilirken liste verilemez!!!!!!!!!!!!!!
# Value discitonary ve list içerebilir.


# ##### Methods

# In[62]:


id.keys() #d.keys() d dictinin keylerini getirir.


# In[63]:


id.values() #d.values() d dictinin valuelerini getirir.


# In[64]:


id.items() #d.items() bütün itemleri getiriyor


# In[66]:


id.get("from") #d.get(x) d dictinin keyi x olan değerinin valuesini verir. 
#Valueleri için olanı kullanılamaz.


# In[67]:


id.update({"Zodiac":"Cancer"}) #dicte yeni bir key (k) ve bir value(v) ekler.
id


# In[69]:


id_copy=id.copy()
id_copy


# In[70]:


id.pop("inf") #d.pop(n) n keyini ve valuesini siler.


# In[71]:


id


# ### Tuples ( )

# Değiştirilemezler.
# 
# Indexleri vardır. 
# 
# Birleştirme yapılabilir.

# In[72]:


zamirler = ("ben","sen","o","biz","siz","onlar")


# In[73]:


zamirler[0]


# In[74]:


zamirler[0]="ten"


# In[75]:


zamirler[-3:-1]


# In[76]:


len(zamirler)


# In[77]:


sayilar= (1,2,4,6,7)


# In[78]:


zamirler + sayilar 


# In[79]:


sayilar.count(7)


# In[80]:


sayilar.index(4)


# In[120]:


tuple1=(4) # Burada eşitleme yapıyor tuple olarak görünmüyor.
print(tuple1)
type(tuple1)


# In[121]:


tuple2=(4,) #Bu şekilde , bırakırsak 1 elemanlı bir tuple oluşturur.
print(tuple2)
type(tuple2)


# ### Sets { }

# İndexli şekilde değildir.Sırasızdır.
# 
# Birbirinden farklı elemanlar içerir. (Aynı elemanlar dahil etmez.)
# 
# Değişiklik yapılarbilir.

# In[81]:


sayi = {1,3,4,6,10,84,7,5,56}


# In[82]:


sayi[1]


# In[83]:


sayi.add(100) #d.add(n) n elemanını d kümesinin sonuna ekler.
sayi


# In[84]:


sayi.discard(7) #d.discard(n) n elemanını kümeden cıkarır.
sayi


# In[85]:


sayi.remove(4) #d.removen) n elemanını kümeden cıkarır.
sayi 


# In[87]:


yenisayilar={11,31,41,51,61,101,561,841,1001}
sayi.update(yenisayilar) #d.update(s) d kümesine s kümesini ekler.
sayi


# In[88]:


k={1,2,4,6}
l={4,5,6,8,9}


# In[89]:


k.difference(l) #d.difference(s) d kümesinin s kümesinden farkını bulur.


# In[90]:


k.intersection(l) #d.intersection(s) d kümesinin s kümesi ile ortak elemanlarını bulur.


# In[91]:


k.union(l) #d.union(s) d kümesi ile s kümesini birleştirir.


# In[92]:


len(k)


# ### Type

# In[93]:


a=9
type(a)


# In[94]:


a=9.9
type(a)


# In[98]:


c=str(a)


# In[96]:


b="5.7"


# In[99]:


c+b


# In[100]:


a+b


# In[107]:


d=float(b)
print(d)
type(d)


# In[108]:


int(d)


# In[109]:


x= [3,6,8,9,4,3]
type(x)


# In[110]:


tuple(x)


# In[112]:


set(x) #2 üç vardi bir 3 e düştü set özelliği


# In[113]:


#Dic haline getirilemez halde oldugundan uygulanamaz


# In[114]:


dict(x=7,y=9)


# In[115]:


t=(5,7,4,8,3)


# In[117]:


y=list(t)
type(y)

