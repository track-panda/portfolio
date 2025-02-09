import math 

celsius = float(input("Give me a temperature in Celsius.").strip())
def celsius_to_farhenheit(celsius):
    return celsius * (9/5) + 32
print(celsius_to_farhenheit(celsius))

farhenheit = float(input("Give me a temperature in Farhenheit.").strip())
def farhenheit_to_celsius(farhenheit):
    return (farhenheit - 32) * (5/9)
print(farhenheit_to_celsius(farhenheit))

radius = float(input("Give me the radius of a circle.").strip())
def area_of_a_cricle(radius):
    return (radius ** 2) * math.pi
print(area_of_a_cricle(radius))

length = float(input("Give me the length of a rectangle.").strip())
width = float(input("Give me a width of a rectangle.").strip())
def area_of_rectangle(length, width):
    return length * width
print(area_of_rectangle(length, width))

base = float(input("Give me the base of the triangle.").strip())
height = float(input("Give me the height of a triangle.").strip())
def area_of_triangle(base, height):
    return (base * height) / 2
print(area_of_triangle(base,height))


number = int(input("Give me a whole number.").strip())
def is_number_even(number):
    return (number % 2)
if number % 2 == 0:
    print("The number you chose is even!")
elif number % 2 != 0:
    print("The number you chose is odd!")

#HOW I DID IT
number_1 = int(input("Give me a whole number.").strip())
number_2 = int(input("Give me a second whole number.").strip())
number_3 = int(input("Give me a third whole number.").strip())
def find_max_number(number_1, number_2, number_3):
    return max(number_1, number_2, number_3)
print(find_max_number(number_1, number_2, number_3))

#HOW HE DID IT
def function_max (a,b,c):
    if a == b and b == c:
        print("All numbers are the same.")
    elif a > b and a > c:
        print(a,"is the biggest.")
    elif b > a and b > c:
        print(b,"is the biggest.")
    elif c > a and c > b: 
        print(c,"is the biggest.")
    elif a == b and a > c:
        print(a, "and",b," are the same and greater than c.")
    elif a == c and a > b:
            print(a, "and",c," are the same and greater than b.")
    elif b == c and b > a:
        print(b, "and",c," are the same and greater than a.")
        