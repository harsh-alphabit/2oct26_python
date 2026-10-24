def Person(id,name,city='Rajkot'): #default arg.
    print("ID:",id)
    print("Name:",name)
    print("City:",city)

# Person(101,'harsh')

# Person(12,'ved','Jamnagar') #positional arg.
Person(name='harsh',id=78, city="jamnagar") #keyword arg.