greet="my name is harsh"

vowel=0
consonent=0
space=0
for char in greet:
    if char in "aeiou":
        vowel+=1
    '''elif char.isalpha():
        consonent+=1
    elif char == " ":
        space+=1'''
else:
    consonent+=1

print(vowel)
print(consonent)
'''print(space)'''