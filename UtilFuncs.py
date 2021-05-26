import math as m

pi = m.pi
e = m.e

#Perimiters
def square_perimiter(side):
      return side * 4
  
def triangle_area(a, b, c):
      return a + b + c
    
def circle_perimiter(radius):
      return 2 * pi * radius
    
def polygon_perimiter(side_len, sides):
      return side_len * sides
    
def trapezoid_perimiter(a, b, c, d):
      return a + b + c + d

#Areas
def square_area(side):
      return side * side

def triangle_area(b, hb):
      return (b * hb) / 2
    
def circle_area(radius):
      return pi * (radius * radius)
    
def polygon_area(perimiter, apothem):
      return (perimiter * apothem) / 2
    
def trapeziod_area(height, base1, base2=None):
      if (base2 == None):
            base2 = base1
      return ((base1 + base2) / 2) * height

# Distance between 2 points
def dist(point1, point2=(0, 0)):
  return m.sqrt(m.pow(point1[0]-point2[0], 2) + m.pow(point1[1]-point2[1], 2))
