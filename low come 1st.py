""" 4. (3)arrange String characters such that lowercase letters should come first"""

message = input('Type here: ')
a = []
b = []
for i in message:
    if i.islower():
        a.append(i)
    elif i.isupper():
        b.append(i)
for j in b:
    a.append(j)
g = ''.join(a)
print(g)