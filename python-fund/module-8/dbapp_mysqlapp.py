import pymysql

try:
    db=pymysql.connect(host="localhost",user="root",password="",database="python")
    print("DataBase Connected")
except Exception as e:
    print(e)
    
    
cr=db.cursor()

#Table Create
tbl_create="create table studinfo(id integer primary key auto_increment, name varchar(20),sub varchar(20))"
try:
    cr.execute(tbl_create)
    print("Table Created")
except Exception as e:
    print(e)

#Insert Data
insert_data="insert into studinfo(name,sub) values('harsh','python'),('nirav','java'),('hitesh','html'),('ashok','php'),('rohan','css')"
try:
    cr.execute(insert_data)
    db.commit()
    print("Data Inserted")
except Exception as e:
    print(e)
