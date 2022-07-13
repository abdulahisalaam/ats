from fractions import Fraction as frac
class Rational_numbers:
    def __init__(self, numerator_a=0,numerator_b=0,denominator_a=0,denominator_b=0):
        self.numerator_a = numerator_a
        self.numerator_b = numerator_b
        self.denominator_a = denominator_a
        self.denominator_b = denominator_b

    def gcd(self,n, d):
            while d != 0:
                t = d
                d = n%d
                n = t
            return n
    
    def reducefract(self,n, d):
        '''Reduces fractions. n is the numerator and d the denominator.'''
        self.gcd(n, d)
        assert d!=0, "integer division by zero"
        assert isinstance(d, int), "must be int"
        assert isinstance(n, int), "must be int"
        greatest=self.gcd(n,d)
        n/=greatest
        d/=greatest
        return frac(int(n),int(d))
    
    def add_fraction(self,numerator_a,numerator_b,denominator_a,denominator_b):
        if denominator_a == denominator_b:
            lcm = numerators_a
            product_a = denominator_a * numerator_a
            product_b = denominator_a * numerator_b
            addition = product_a + product_b
            return self.reducefract(addition, denominator_b)
        else:
            lcm = denominator_a * denominator_b
            add = numerator_a + numerator_b
            return self.reducefract(add, lcm)

    def multiply_fraction(self,numerator_a,numerator_b,denominator_a,denominator_b):
        num = numerator_a * numerator_b
        deno = denominator_a * denominator_b
        return self.reducefract(num, deno)
    
    def divide_fraction(self,numerator_a,numerator_b,denominator_a,denominator_b):
        num = numerator_a * numerator_b
        deno = denominator_a * denominator_b
        return self.reducefract(num, deno)

    def float_fraction(self,numerator_a,denominator_a):
        return numerator_a/denominator_a

r = Rational_numbers()
print(r.multiply_fraction(2,15,2,17))
# print(r.float_fraction(1,3))
        