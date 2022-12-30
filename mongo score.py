#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo


# In[2]:


client = pymongo.MongoClient("mongodb://embifiAdmin:embifi_1659709763@db.embifi.in:22058/embifi-native?authMechanism=DEFAULT&authSource=admin")


# In[3]:


db = client['lms']


# In[4]:


collection = db['collection_schedules']


# In[5]:


print(collection)


# In[6]:


alldocs = collection.find({"collection_id": "COL16702385573808265"})
for x1 in alldocs:
    print(x1)


# In[7]:


collection.count_documents(filter= {"collection_id": "COL16702385573808265"})


# In[8]:


def find_any(_id):
    cust_id = _id
    person = collection.find({'collection_id': cust_id},
                             {'_id': 0, 'edi_number':1, 'edi_amount':1, 'collected_amount':1,'os_principal':1})
    
    for x1 in person:
        print(x1)


# In[9]:


find_any("COL16702385573808265")


# In[10]:


type(x1)


# In[11]:


def count_ppl(_id):
    cust_id = _id
    count= collection.count_documents(filter={'collection_id': cust_id})
    print(count)


# In[12]:


x = count_ppl("COL16702385573808265")


# In[13]:


count_ppl("COL1670396188214391")


# In[14]:


count_ppl('COL16703967139273536')


# In[ ]:





# In[30]:


all_records = collection.find({'collection_id': 'COL16703967139273536'})


# In[31]:


lst = list(all_records)


# In[32]:


import numpy as np
import pandas as pd


# In[33]:


df = pd.DataFrame(lst)


# In[34]:


df.head()


# In[35]:


X1= df['edi_amount'].sum()
print(X1)


# In[36]:


df['collected_amount'].sum()


# #### X12 to X17 : amount to be paid (bill amount)

# In[37]:


X12 = df['edi_amount'].loc[:29].sum()
print(X12)


# In[38]:


X13 = df['edi_amount'].loc[30:59].sum()
print(X13)


# In[39]:


X14 = df['edi_amount'].loc[60:89].sum()
print(X14)


# In[40]:


X15 = df['edi_amount'].loc[90:119].sum()
print(X15)


# In[41]:


X16 = df['edi_amount'].loc[120:149].sum()
print(X16)


# In[42]:


X17 = df['edi_amount'].loc[150:179].sum()
print(X17)


# #### X18 to X23 : amount paid by the customer

# In[43]:


X18 = df['collected_amount'].loc[:29].sum()
print(X18)


# In[44]:


type(X18)


# In[45]:


X19 = df['collected_amount'].loc[30:59].sum()
print(X19)


# In[46]:


X20 = df['collected_amount'].loc[60:89].sum()
print(X20)


# In[47]:


X21 = df['collected_amount'].loc[90:119].sum()
print(X20)


# In[48]:


X22 = df['collected_amount'].loc[120:149].sum()
print(X20)


# In[49]:


X23 = df['collected_amount'].loc[150:179].sum()
print(X20)


# month6_pay =  df['os_principal'].loc[179:179].sum()
# print(month6_pay)

# In[ ]:





# In[87]:


a = (X12 - X18)
b = (X13+X12)-(X18+X19)
c = (X12+X13+X14)-(X18+X19+X20)
d = (X12+X13+X14+X15)-(X18+X19+X20+X21)
e = (X12+X13+X14+X15+X16)-(X18+X19+X20+X21+X22)
f = (X12+X13+X14+X15+X16+X17)-(X18+X19+X20+X21+X22+X23)

print(a,b,c,d,e,f)


# In[88]:


a= (X12 - X18)
def value_X6():
    X6 = -1
    if a<X12:
        print(X6)
    if a>= X12:
        print(X6+2)  


# In[89]:


value_X6()


# In[90]:


b= (X13+X12)-(X18+X19)
def value_X7():
    X7 = -1
    if b< X13:
        print(X7)
    if b>= X13:
        print(X7+2)  
    if b>=2*(X13):
        print(X7+3)


# In[91]:


value_X7()


# In[92]:


c = (X12+X13+X14)-(X18+X19+X20)
def value_X8():
    X8 = -1
    if c< X14:
        print(X8)
    if (X14<c<2*(X14)):
        print(X8+2)  
    if (2*(X14)<c<3*(X14)):
        print(X8+3)
    if (3*(X14)<c<4*(X14)):
        print(X8+4)


# In[93]:


value_X8()


# In[94]:


d = (X12+X13+X14+X15)-(X18+X19+X20+X21)
def value_X9():
    X9 = -1
    if d< X15:
        print(X9)
    if (X15<d<2*(X15)):
        print(X9+2)  
    if (2*(X15)<d<3*(X15)):
        print(X9+3)
    if (3*(X15)<d<4*(X15)):
        print(X9+4)
    if (4*(X15)<d<5*(X15)):
        print(X9+5)
    if (5*(X15)<d<6*(X15)):
        print(X9+6)


# In[95]:


value_X9()


# In[96]:


e = (X12+X13+X14+X15+X16)-(X18+X19+X20+X21+X22)
def value_X10():
    X10 = -1
    if e< X16:
        print(X10)
    if (X16<e<2*(X16)):
        print(X10+2)  
    if (2*(X16)<e<3*(X16)):
        print(X10+3)
    if (3*(X16)<e<4*(X16)):
        print(X10+4)
    if (4*(X16)<e<5*(X16)):
        print(X10+5)
    if (5*(X16)<e<6*(X16)):
        print(X10+6)
    if (6*(X16)<e<7*(X16)):
        print(X10+7)


# In[97]:


value_X10()


# In[98]:


f = (X12+X13+X14+X15+X16+X17)-(X18+X19+X20+X21+X22+X23)
def value_X11():
    X11 = -1
    if f< X17:
        print(X11)
    if (X17<d<2*(X17)):
        print(X11+2)  
    if (2*(X17)<f<3*(X17)):
        print(X11+3)
    if (3*(X17)<f<4*(X17)):
        print(X11+4)
    if (4*(X17)<f<5*(X17)):
        print(X11+5)
    if (5*(X17)<f<6*(X17)):
        print(X11+6)
    if (6*(X17)<f<7*(X17)):
        print(X11+7)
    if (7*(X17)<f<8*(X17)):
        print(X11+8)
    


# In[99]:


value_X11()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




