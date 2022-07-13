class Rectangle:
    def __init__(self,length = 1,width = 1):
        self.__length = length
        self.__width = width

    def get_area_rectangle(self):
        return f"The area of the rectangle {(self.__length) * (self.__width)}"

    def get_parimeter_rectangle(self):
        return f"The perimeter of the rectangle is {2*(self.__length + self._width)}"

    def get__width(self):
        return self.__width
    
    def get__length(self):
        return self.__length
    
    #setter method
    def set__width(self,w):
        self._width = w
        return self.__width
    
    def set__length(self,l):
        self.__length = l
        return self.__length

r = Rectangle()

r.set__length(23)
r.set__width(23)
print(r.get_area_rectangle())
print(r.get_parimeter_rectangle())
    