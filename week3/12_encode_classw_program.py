import string
def encode(data:str):
    digits= string.digits
    special_chars = string.punctuation #all special characters
    alpha_lower = string.ascii_lowercase # a,b,c,d,e, ...z
    alpha_upper = string.ascii_uppercase # A,B,C,D,E ...Z
    reversed_alpha_lower = alpha_lower[::-1] # z,y,x,w,...a
    vowels= ['a','e','i','o','u']
    vowels_map = ['#','$','%','&','*']

    enc = list(), # or []

    for s in data:
        if s.lower() in vowels:
            enc.append(vowels_map[vowels.index(s)])
        elif s in special_chars:
            enc.append('|' + s)
        elif s in alpha_lower + alpha_upper:
            enc.append(s.swapCase())
        #else:
    return ''.join(enc)
    
print(encode('aiuAA'))


