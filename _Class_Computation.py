
# 1 - Create a Computation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
# 2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
# 3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
# 4 - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
# 4 - Create  a method called testPrims() allowing to test if two numbers are prime between them.
# 5 - Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# 6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.

class Computation:
    def __init__(self):
        pass
    
    @classmethod
    def factorial(cls,number):
        if number == 1:
            return 1
        else:
            return number * factorial(number-1)

    @classmethod
    def sum(cls,number):
        if number == 1:
            return 1
        else:
            return number + factorial(number-1)

    @classmethod
    def is_prime(cls,number):
        p = any(n for n in [num for num in range(2,number)] if number % n == 0)
        if p:
            return False
        return True

        
    
    @classmethod
    def testprims(cls,*number):
        nums = []
        for num in number:
            if Computation.is_prime(num) and num > 1:
                nums.append(f"{num} is a Prime number\n")
        return "".join(nums)
    
    @classmethod
    def tablemult(cls,number,rang):
        result2 = []
        numbers = [nums for nums in range(1,rang+1)]

        for key,value in enumerate(numbers):
            # print(f"{number} X {key} = {(value * number)}")
            result2.append(f"| {number} X {key+1} | {(value * number)} \n")
        return "".join(result2)

    @classmethod
    def allTablesMult(cls):
        result2 = []
        numbers = [nums for nums in range(1,10)]
        print(numbers)

        for key,value in enumerate(numbers):
            # print(f"{number} X {key} = {(value * number)}")
                result2.append(f"| {value} X {key+1} | {(value)} \n")
        return "".join(result2)

        @staticmethod
        def list_div(number):
            Ldiv = [n for n in [num for num in range(2,number)] if number % n == 0]
            return p

        def listDivPrim():
            pass


u = Computation()

#print(u.tablemult(4,15))
# print(u.testprims(3,0,2,4,5,6,8,7,10,1,17,18,29,30,31,35))
# print(u.is_prime(15))
# print(u.allTablesMult())
print(Computation.listdiv(8))

    

