id=input("Enter an ID:")
name=input("Enter a Name:")
city=input("Enter a City:")

fl=open("temp.txt","w")

fl.write(f"ID:{id}\nName:{name}\nCity:{city}")