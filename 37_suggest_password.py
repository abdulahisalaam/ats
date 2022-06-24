import string
import random
def suggest_password():
    string_p = string.punctuation
    string_c = string.ascii_lowercase
    string_t = string.ascii_uppercase
    a = string_p.split('',3)
    x = random.sample(a, 5)
    # b= random.shuffle(string_c.split(','))
    # c= random.shuffle(string_t[1:5].split(','))
    return f'{x}'
print(suggest_password())

    
 