import sqlite3

try:
    db=sqlite3.connect('demo.db')
    print("Database created successfully")
except Exception as e:
    print(e)
    
    
#Table Creation
tbl_create="create table studinfo(id integer primary key autoincrement,name text,city text)"

try:
    db.execute(tbl_create)
    print("Table created successfully")
except Exception as e:
    print(e)
    


#Insert Data
ins_data="insert into studinfo(name,city) values('harsh','Rajkot')"
try:
    db.execute(ins_data)
    db.commit()
    print("Data inserted successfully")
except Exception as e:
    print(e)

