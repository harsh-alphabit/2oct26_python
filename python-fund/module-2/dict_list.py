menu={
    1:("pizza",250),
    2:("burger",150.50),
    3:("garlic bread",200),
    4:("drink",25),
    }

selected=[]

while True:

    choice=int(input("select what u want to eat: "))

    if choice == 1:
        selected.append(menu[1])
    elif choice == 2:
        selected.append(menu[2])
    elif choice == 3:
        selected.append(menu[3])
    elif choice == 4:
        selected.append(menu[4])
    elif choice == 5:
        break
    else:
        print("invalid choice")

print(selected)