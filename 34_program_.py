def convert_to_ordinal(num:int):

    if num % 10== 0:
        return f'{num}th'
    elif num % 10==1:
        return f'{num}st'
    elif num % 10==3:
        return f'{num}rd'
    elif num % 10 == 4:
        return f'{num}th'
    elif num //10 == 0:
        return f'{num}th'
    elif num == 12:
        return f'{num}th'
    else:
        return f'{num}th'

print(convert_to_ordinal(31))