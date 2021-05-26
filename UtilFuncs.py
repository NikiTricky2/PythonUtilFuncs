import math as m

pi = m.pi
e = m.e

#Perimeters
def square_perimeter(side):
      return side * 4
    
def rectangle_perimeter(side1, side2):
      return (side1 + side2) * 2
  
def triangle_area(a, b, c):
      return a + b + c
    
def circle_perimeter(radius):
      return 2 * pi * radius
    
def polygon_perimeter(side_len, sides):
      return side_len * sides
    
def trapezoid_perimeter(a, b, c, d):
      return a + b + c + d

#Areas
def square_area(side):
      return side * side

def rectangle_area(side1, side2):
      return side1 * side2

def triangle_area(b, hb):
      return (b * hb) / 2
    
def circle_area(radius):
      return pi * (radius * radius)
    
def polygon_area(perimeter, apothem):
      return (perimeter * apothem) / 2
    
def trapeziod_area(height, base1, base2):
      return ((base1 + base2) / 2) * height

# Distance between 2 points
def dist(point1, point2=(0, 0)):
  return m.sqrt(m.pow(point1[0]-point2[0], 2) + m.pow(point1[1]-point2[1], 2))
