#!/usr/bin/env python
# coding: utf-8

# # PYTHON EXERCISE

# ### 1. JUPYTER notebook ta kısayolları kullanarak aşağıdaki satırın bir üstüne satır ekleyip "python egsersizleri" yazan bir başlık ekleyin

# # python egsersizleri

# In[ ]:





# ### 2."Merhaba ben Tek" çıktısı veren String yani bir karakter dizisi oluşturup "x" değişkenine atayın ve len() fonksiyonunu kullanarak karakter dizisinin uzunluğunu belirleyin

# In[1]:


x="Merhaba ben Tek"
len(x)


# In[5]:





# ### 3.
# ###   isim = "Mehmet"
# ###   soyisim = "Tek"
# ###   isim ve soyisim değişkenlerini ve format() metodunu kullanarak ekrana "benim ismim Mehmet Tek" çıktısını verin

# In[27]:


isim= "Mehmet"
soyisim="Tek"

a=str("benim ismim {} {}".format(isim,soyisim))
print(a)


# In[35]:





# ### 4.Üstte oluşturduğunuz "benim ismim Mehmet Tek" çıktısını veren değişkeni split() metodunu kullanarak kelimelerine ayırın

# In[28]:


a.split()


# In[9]:





# ### 5.Elemanları  ["ömer",34,56,78,90,[4,5,6],89]  olan bir liste oluşturun.  listenize append() metodunu kullanarak "ali" yi ekleyin ve listeden "90" elemanını indexini kullanarak çekin

# In[24]:


xyz=["ömer",34,56,78,90,[4,5,6],89]
xyz.append("ali")
print(xyz)
xyz[4]


# In[15]:





# ### 6.Elemanları [4,6,3,8,1,0] olan bir liste tanımlayın ve listenin küçükten büyüğe olmasını sort() metodunu kullanarak sağlayın.

# In[ ]:


Çıktıların kaybolmaması için kodunuzu buraya yazınız


# In[17]:





# ### 7. Elemanları "ali" : 34 ,"ahmet": 35 , "kemal" : 45 ,"mustafa" : 55 olan bir sözlük oluşturup keys() metoduyla bütün anahtarları çekin ,values() metoduyla da bütün değerleri çekin

# In[5]:


x={"ali":34,"ahmet":35,"kemal":45,"mustafa":55}
print(x.keys())
print(x.values())


# In[21]:





# ### 8. İnput() fonksiyonunu kullanarak kullanıcıdan "notunuzu girin = " yazısına cevap vermesini isteyin. Verdiği cevaba göre IF ,ELIF ve ELSE koşullu ifadesini kullanarak 90 ile 100 arasında ise " notunuz A",   80 ile 90 arasında ise " notunuz B" ,  70 ile 80 arasında ise " notunuz C" ,  60 ile 70 arasında ise " notunuz D" ,  60 ın altında ise "Notunuz F " ,  eğer  0 ile 100 arasında bir değer girmezse  " Yanlış girdiniz " yazısını çıktı veren bir kod yazınız

# In[9]:


grade=int(input("notunuzu girin ="))
if 90<=grade<=100:
    print("Notunuz A")
elif 80<=grade<90:
    print("Notunuz B")
elif 70<=grade<80:
    print("Notunuz C")
elif 60<=grade<70:
    print("Notunuz D")
elif 0<=grade<60:
    print("Notunuz F")
else:
    print("Yanlış girdiniz.")


# In[30]:





# ### 9. Verdiğiniz sayının küpünü alan bir fonksiyon yazınız (Def , Return) ve bu fonksiyonu kullanarak 4 ün küpünü alınız

# In[11]:


def cube(x):
    return x**3

print(cube(4))


# In[31]:





# ### 10. Lambda kısayol fonksiyon oluşturma ifadesini kullanarak sayının karesini alan bir fonksiyon yazınız ve bu fonksiyonla 10 un karesini alınız

# In[12]:


dk= lambda x : x**2
print(dk(10))


# In[32]:





# ### 11. Bir "a" değişkeni atayıp "0" değerini verin. While döngüsünü kullanarak her döngüde bir artmasını sağlayarak 10 a kadar döndürün.

# In[19]:


a=0
i=0
while i in range(0,10):
    a+=1
    print(a)
    i+=1
    
'''
a = 0

while a < 10:
    a += 1
    print(a)

'''


# In[33]:





# ### 12. For döngüsünü ve range() fonksiyonunu kullanarak 0 den 101 e kadar olan sayıları 5 er artarak yazdırın. 

# In[23]:


z=0

for z in range(0,102):
    if z%5==0:
        print(z)
        
'''
for i in range(0,101,5):
    print(i)
'''


# In[34]:





# In[ ]:


#Doğukan Kaan Bozkurt

