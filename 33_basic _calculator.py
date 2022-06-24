def basic_calculate(option,*inputs):
    result = 0
    for x in inputs:
        if option == '*':
            if result <= 0:
                result = 1
            result *=x  
        elif option == '+':
            result += x
        elif option == '-':
            result -=x
        elif option == '/':
            if result == 0:
                result = 1
            result /=x
    return result
print(basic_calculate('/',6,2,4))
