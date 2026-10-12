name = input("enter your name:")

count=0 

for ch in name:
    count +=1

while count>0:
    print(name[count-1],end="")
    count-=1

    