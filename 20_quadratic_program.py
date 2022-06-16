def find_quadratic_equation(a:int,b:int,c:int):
    product_of_ac = a*c
    factors =[i for i in range(-abs(product_of_ac),abs(product_of_ac)+1) if i != 0 and product_of_ac % i == 0]

    final_factors= [factor for factor in factors for i in range(len(factors)) if factor + factors[i] == b and factor * factors[i]== c]

    return ' and '.join(str(x) for x in final_factors)



print(find_quadratic_equation(1,8,12))
