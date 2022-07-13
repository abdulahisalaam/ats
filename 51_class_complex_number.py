class Complex_numbers:
    def __init__(self,realpart:float=None,imaginarypart:float=None):
        self.realpart = realpart
        self.imaginarypart = imaginarypart

    def add_realpart(self,*values):
        realpart = sum(values)
        return realpart

    def add_imaginarypart(self,*values):
        imaginarypart = sum(values)
        return imaginarypart

    def subtract_realpart(self,*number):
        for num in number:
            realpart = num - num
        return realpart
    
    def subtract_imaginarypart(self,*number):
        for num in number:
            imaginarypart = num - num
        return imaginarypart

    def add_complex(self):
        return f"{self.add_realpart(1,2)} + {self.add_imaginarypart(3,5)}i"

    def subtract_complex(self):
        return f"{self.subtract_realpart(3,2)} - {self.subtract_imaginarypart(3,2)}i"
    
    
c = Complex_numbers()

print(c.add_complex())
print(c.subtract_complex())
