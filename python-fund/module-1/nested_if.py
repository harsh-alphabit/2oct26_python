age=int(input("enter your age : "))

if age>18:
    print("eligable for vote")
    if age>60:
        print("user is senior")
    else:
        print("user not a senior")

else:
    print("not eligable for vote")