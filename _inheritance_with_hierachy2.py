from _inheritance_with_hierachy1 import Shape

class Two_dimensional_shape(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width
        

class Circle(Two_dimensional_shape):
    pi=2.27 
    def __init__(self,length,width,radius):
        super().__init__()
        self.length = length
        self.width = width
        self.radius = radius

    def area_circle(self):
        return f'the Area of circle is {2 * (Circle.pi * self.radius)}'

    def perimeter_circle(self):
        return f'the Perimeter of the circle is: {(Circle.pi * self.radius)}'


class Square(Two_dimensional_shape):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area_square(self):
        return f'the Area Square is {(self.length * self.width)}'

    def perimeter_square(self):
        return f'the Perimeter of the square is: {( 2 *(self.length + self.width))}'


class Triangle(Two_dimensional_shape):
    def __init__(self,length,width,height):
        super().__init__()
        self.length = length
        self.width = width
    
    def area_tri(self):
        return f'the Area Triangle is {(self.width * self.height) * 0.5}'

    def perimeter_tri(self):
        return f'the Perimeter of the triangle is: {( (self.length + self.width + self.height))}'