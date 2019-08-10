""" 3. (3)Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string"""
s1 = 'jaihind'
s2 = 'chennai'
a = []
b = []
for i in s1:
    a.append(i)
for j in s2:
    b.append(j)
c = len(a) / 2
if c % 2 == 0:
    e = c
else:
    e = c - 0.5
f = int(e)
del b[:f]
del b[-f:]
del a[:f]
del a[-f:]
g = ' '.join(b)
h = ' '.join(a)
print(f"'s1 first: ' {s1[0]} 'middle:' {h} 'last:'{s1[-1]}")
print(f"'s2 first: ' {s2[0]} 'middle:' {g} 'last:'{s2[-1]}")