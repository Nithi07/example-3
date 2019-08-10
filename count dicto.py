""" 9. (3)Given an input string, count occurrences of all characters within a string
and return a dict with the character as key and count as value
"""

message = input('Type here: ')
a = 0
b = {}
for i in message:
    if i.isalpha():
        a += 1
        b[i] = a
print(b)