
import string

alpha = string.ascii_lowercase
vowels = 'aeiou'
#(1a) 
print(alpha[0:10])

#(2a)
print(alpha[-11:-1])

#
consonant = ''.join([x for x in alpha if x.lower() not in vowels])
print(f"consonants are {consonant}")

def vowels_p():
    new=[]
    for i in alpha:
        if i in vowels:
            new.append(i)
    return ''.join(new)

print(f"vowels are {vowels_p()}")
    
# def consonant():
#     vowels = 'aeiou'
#     new=[]
#     for i in alpha:
#         if i not in vowels:
#             new.append(i)
#     return ''.join(new)

# consonant()

#(2)(a)
vowel = vowels_p()
print(','.join(vowel))

print(','.join(consonant))

print('\n')

#3(b)
def check_case(word):
    if word.islower():
        return f'it is lower case'
    elif word.isupper():
        return f"it is upper case"
    else:
        return f"it is mixed case"

print(check_case('worD'))

#(4)

def func_dict(dicto):
    for k,v in enumerate(dicto):
        return f"{k} is the key, and {v} is the value"

#(5)



    
    















