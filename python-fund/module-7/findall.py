import re

mystr="This is Python!"

x=re.findall("python",mystr)
print(x)

if x:
    print("Match done!")
else:
    print("Error!")