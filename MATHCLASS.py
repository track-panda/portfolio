class Math:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def addition(self):
        return self.a + self.b + self.c
    
    def subtraction(self):
        return self.a - self.b - self.c 

    def multiplication(self):
        return self.a * self.b * self.c
    
    def division(self):
        return self.a / self.b / self.c
    
    def exponent(self):
        return self.a ** self.b
    
    def perimeter(self):
        return (self.a * 2) + (self.b * 2)
    
    def area(self):
        return self.a * self.b
    
    def area_triangle(self):
        return (self.a * self.c) / 2
    
    def volumne_sphere(self):
        return ((self.b ** 3) * 3.14) * 4/3
    
    def surface_area(self):
        return (6 * ((self.c * self.b) ** 2))
    
    def sin0(self):
        return (self.a / self.c)
    
    def cos0(self):
        return (self.b / self.c)
    
    def tan0(self):
        return (self.a / self.b)
    
    def absolute_value(self):
        return abs(self.a)
    
    def square_root(self):
        return (self.c / self.c)
    

math = Math(10,12,15)

print(math.addition())
print(math.subtraction())
print(math.multiplication())
print(math.division())
print(math.exponent())
print(math.perimeter())
print(math.area())
print(math.area_triangle())
print(math.volumne_sphere())
print(math.surface_area())
print(math.sin0())
print(math.cos0())
print(math.tan0())
print(math.absolute_value())
print(math.square_root())