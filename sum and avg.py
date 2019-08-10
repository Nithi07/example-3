"""  8. (3)Given a string, return the sum and average of the digits that appear in the string,
ignoring all other characters
"""
message = input('Enter: ')
a = []
for i in message:
    if i.isdigit():
        a.append(i)
print(sum(a))

#output issue

