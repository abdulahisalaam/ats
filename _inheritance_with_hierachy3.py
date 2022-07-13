from _inheritance_with_hierachy1 import Shape

class Three_dimensional_shape(Shape):
    def __init__(self,length=0,width=0):
        super().__init__()
        self.length = length
        self.width = width


class Sphere(Three_dimensional_shape):
    pi = 2.27
    def __init__(self,radius, width):
        super().__init__()
        self.radius = radius
        self.width = width

    def area_sphere(self):
        return f'the Area Sphere is {(4 * (Sphere.pi * self.radius * self.radius))}'

    def diameter_sphere(self):
        return f'the Perimeter of the sphere is: {( 2 * self.radius)}'


class Cube(Three_dimensional_shape):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width

    def area_cube(self):
        return f'the Area Cube is {(self.length * self.width)}'

    def perimeter_cube(self):
        return f'the Perimeter of the Cube is: {( 2 *(self.length + self.width))}'


class Tetrahedron(Three_dimensional_shape):
    def __init__(self,length=0,width=0):
        super().__init__()
        self.length = length
        self.width = width

    def surface_area_tetrahedron(self):
        return f'the Area Tetrahadron is: {4 * (self.length * self.width)/2}'

    def perimeter_tetrahedron(self):
        return f'the Perimeter of the Tetrahadron is: {( 6 * self.length)}'

s = Tetrahedron(6,7)
print(s.surface_area_tetrahedron())