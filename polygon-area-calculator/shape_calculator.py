class Rectangle:
  def __init__(self, width: int, height: int):
    self.nameOfShape = "Rectangle"
    self.width = width
    self.height = height
    

    
  def set_width(self,new_width):
    self.width=new_width

  def set_height(self,new_height):
    self.height=new_height

  def get_area(self):
    self.area= self.width * self.height
    return (self.area)

  def get_perimeter(self):
    self.perimeter=2 * self.width + 2 * self.height
    return (self.perimeter)

  def get_diagonal(self):
    self.diagonal=(self.width ** 2 + self.height ** 2) ** .5
    return (self.diagonal)

  def get_picture(self):
    picture=[]
    if self.height>=50 or self.width>=50:
      return("Too big for picture.")
    else:
      for i in range(0,self.height):
        picture.append(self.width*"*"+"\n")
      return (''.join(picture))

  def get_amount_inside(self,other):
    return (self.width//other.width )*(self.height//other.height)

  def __str__(self):
    return("Rectangle(width="+str(self.width)+', height='+str(self.height)+')')






class Square(Rectangle):
  def __init__(self,side):
    Rectangle.__init__(self, side, side)
    self.nameOfShape = "Square"

  def set_side(self, new_side):
    self.width=new_side
    self.height=new_side

  def __str__(self):
    return("Square(side="+str(self.width)+')')
    
     


  
