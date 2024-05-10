#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install psycopg2')
import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='Madhuneha', host='localhost', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql = '''CREATE database mydb''';

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()


# In[ ]:




