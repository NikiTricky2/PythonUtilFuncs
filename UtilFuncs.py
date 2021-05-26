import math as m

# Distance between 2 points
def dist(point1, point2=(0, 0)):
  return m.sqrt(m.pow(point1[0]-point2[0], 2) + m.pow(point1[1]-point2[1], 2))
