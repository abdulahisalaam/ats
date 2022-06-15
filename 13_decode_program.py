import string

def decode(data:str):
    digits = string.digits
    speci_str= string.punctuation
    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    reversed_apha_lower = alpha_lower[::-1]

    vowel_map=['#','$','%','&','*']
    vowel =['a','e','i','o','u']
    speci_map = ['^','|','(',')','@']
    
    dec = list()

    for s in data:
        if s in vowel_map:
            dec.append(vowel[vowel_map.index(s)])
        elif s in speci_str:
            dec.append(s)
        elif s in speci_map:
            dec.insert(data.index(s), data.index(s + 1))
        elif s in alpha_lower + alpha_upper:
            dec.append(s.swapcase())

    return ''.join(dec)
print()
print(decode('#%*|%&**()'))

print()
