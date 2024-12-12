# import math
import math
# This is the parent class used in this code segment
class shape:
  def __init__(self):
    # mambers are no of sides area and perimeter
    self.sides=0
    self.area=0
    self.pericirc=0
  # functions for printing area and perimeter
  def printArea(self):
    print("The area  is :",self.area)
    
  def printCirc(self):
    print("The perimeter of this shape is :",self.pericirc)
    
#This is the rectangle child class
class rectangle(shape):
  pass
  # constructor
  # initialize all the elements
  def __init__(self,l,b):
    self.l=l
    self.b=b
    self.area=l*b
    self.pericirc=2*(l+b)
    self.sides=2
  # functions to calcualte area and perimeter
  def area(self):
    return l*b
  def perimeter(self):
    return 2*(l+b)
  
# This is the circle child class
class circle(shape):  
  pass
# constructor
  # initialize all the elements
  def __init__(self,r):
    self.r=r
    self.area=math.pi*(r**2)
    self.pericirc=2*(math.pi*r)
    self.sides=1
  # functions to calcualte area and perimeter
  def area(self):
    return math.pi*(r**2)
  def circ(self):
    return 2*(math.pi*r)
    
#main function
def main():
 
  # make objects of type circle and rectangle
  c=circle(5)
  r=rectangle(5,5)

  # call the functions and print the area and perimeter
  print("For child class rectangle")
  r.printArea()
  r.printCirc()
  print("For child class circle")
  c.printArea()
  c.printCirc()
  


if __name__=="__main__":
    main()
  
