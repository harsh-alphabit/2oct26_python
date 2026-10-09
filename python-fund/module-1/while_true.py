

initial_ammount=int(input("enter your initial ammount = "))
while True:

    if initial_ammount>0:
        print("="*20)
        print("1) press 1 for deposit")
        print("2) press 2 for withdraw")
        print("4) press 4 for balance")
        print("3) exit")
        choice=int(input("enter your choice here = "))

        if choice == 1:
            deposit=int(input("enter how much you want to deposit = "))
            initial_ammount += deposit

            print(f"your new bank balance after deposit amount ({deposit}) is = {initial_ammount}")

        elif choice==2:
            withdraw=int(input("enter how much you want to withdraw = "))
            initial_ammount -= withdraw

            print(f"your new bank balance after withdraw amount ({withdraw}) is = {initial_ammount}")

        elif choice == 3:
            print("bye bye")
            break

        elif choice == 4:
            print(f"my current balance is {initial_ammount}")

        else:
            print("enter valid choice")

    else:   
        print("insufficient ammount")