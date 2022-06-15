# import string
# def is_pangrams(sentence:str):
#     letters = string.ascii_lowercase
    
#     for i in range(len(letters)):
#         if letters[i] in sentence:
#             result = True
#             result = result * True
#         else:
#             result = False
    
#     if result == True:
#         return f"it a pangram"
#     else:
#         return f"Not a pangram"
        
# print(is_pangrams("abcdefghijklmnopqrstzuvwyx"))



# def check_hyphen_sort(sentence:str): 
#     street = sentence.split('_') 
#     street.sort()
#     return '_'.join(street)
    #           or
    # return '_'.join(sorted(street))

# message = "yellow_green_red_blue_pink_orange"
# print(check_hyphen_sort(message))





# def check_perfect_number(number:int):
#     if (2**number * 1/2 (2**number) + 1) == number:
#         return True
#     else:
#         return False


# num=int(input("Enter a number"))

# check_perfect_number(num)

# street = "6 akera "

# print(''.join(street))
# print('lagos'.split())

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }

print(A.symmetric_difference(B))