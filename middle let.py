""" 1. (3)Given a string of odd length greater 7, return a string made of the middle three chars of a given String"""

a = 'advisor'
b = []
for i in a:
    b.append(i)
c = len(b) / 2
if c % 2 == 0:
    e = c
else:
    e = c-0.5
f = int(e)
del b[:f]
del b[-f:]
g = ' '.join(b)
print(g)

