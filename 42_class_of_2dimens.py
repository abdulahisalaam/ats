import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area_circle(self,radius):
        return f"The area of the circle is {math.floor(2 * math.pi * radius **2)}"
        
    def get_perimeter_circle(self, radius):
        return f"The perimeter of a circle is {2* math.pi}"

        
class Triange:
    def __init__(self):
       pass
    
    def get_area_triangle(self,height,base):
        return f"The area of the Triangle is {self.base * self.height}"

    def get_parimeter(self,base):
        return f"The perimeter of a Triangle {2*base}"
    
class Parallelogram:
    def __init__(self,base = None,height = None,radius = None, angle_between_the_sides= None):
        self.base = base
        self.height = height
        self.angle_between_the_sides = angle_between_the_sides

    def get_area_parallelogram(self,base,height):
        return f"The area of the parallelogram {base * height}"

    def get_parimeter_parallogram(self,base,height):
        return f"The perimeter of the parallelogram is {2*(self.base + self.height)}"


class Kite:
    def __init__(self,short_d,long_d):
        self.short_d = short_d
        self.long_d = long_d

    def get_area_kite(self,short_d,long_d):
        return f"The Area of the Kite is {(self.short_d*self.long_d)/2}"

    def get_perimeter_kite(self, short_d, long_d):
        return f"The perimeter of a Kite is {2*(self.short_d + self.long_d)}"


thing = Circle(3)
print(thing.get_area_circle(3))
print(thing.get_perimeter_circle(3))


