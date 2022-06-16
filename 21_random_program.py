import random
import string
n =int(input('Enter the number of times to print :'))

def func_print_sentence(num:int):

    names =['Lukman','Awal','Toluwani','Bashiru','faith',]
    verbs=['ate','jumped','toast','play','beat']
    objects=['food','fence','bread','piano','Drums']

    
    for n in range(num):
        strings = f'{random.choice(names)} {random.choice(verbs)} {random.choice(objects)}'
        return set(strings)

print(func_print_sentence(n))



