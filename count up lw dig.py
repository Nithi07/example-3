""" 5. (3)Given a string input Count all lower case, upper case, digits, and special symbols
"""
message = input('Type here: ')
tot_upper = 0
tot_lower = 0
tot_digit = 0
tot_space = 0
spe_sym = 0
for i in message:
    if i.isupper():
        tot_upper += 1
    elif i.islower():
        tot_lower += 1
    elif i.isdigit():
        tot_digit += 1
    elif i.isspace():
        tot_space += 1
    else:
        spe_sym += 1
    pass
print(f"total upper cases: {tot_upper}\n total lower cases:  {tot_lower}\n total digits: {tot_digit}\ntotal special symbols: {spe_sym}")
