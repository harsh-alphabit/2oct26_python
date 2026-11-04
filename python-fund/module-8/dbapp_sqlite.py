import sqlite3

try:
    db=sqlite3.connect("my_database.db")
    print("Database connection established successfully.")
except Exception as e:
   print(e)

#Table Create
tbl_create="create table studinfo(id integer primary key autoincrement, name varchar(20), city varchar(20))"
try:
    db.execute(tbl_create)
    print("Table created successfully.")
except Exception as e:
    print(e)
    

#Insert Data
insert_data="insert into studinfo(name,city)values('harsh','pune'),('ashok','baroda'),('hitesh','surat'),('mahesh','gondal'),('hardik','rajkot')"

try:
    db.execute(insert_data)
    db.commit()
    print("Data inserted successfully.")
except Exception as e:
    print(e)
    
#Update Data
'''update_data="update studinfo set name='mitesh', city='junagadh' where id=4"
try:
    db.execute(update_data)
    db.commit()
    print("Data updated successfully.")
except Exception as e:
    print(e)'''
    
#Delete Data
'''delete_data="delete from studinfo where id=5"
try:
    db.execute(delete_data)
    db.commit()
    print("Data deleted successfully.")
except Exception as e:
    print(e)'''

#Select Data
select_data="select * from studinfo"
try:
    cr=db.cursor()
    cr.execute(select_data)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)
    for i in data:
        print(i)
except Exception as e:
    print(e)
    
