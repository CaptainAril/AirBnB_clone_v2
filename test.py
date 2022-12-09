#!/usr/bin/python3

from models.engine.db_storage import DBStorage
st = DBStorage()
dic = st.all('states')
print(dic)
for i in dic:
    i = i.__dict__
    print(i)
