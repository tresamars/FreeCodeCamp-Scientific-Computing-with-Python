import copy
import random
# Consider using the modules imported above.


class Hat:
  def __init__(self,**kwargs):
    self.contents=[]
    for key, value in kwargs.items():
      i=0
      while i < value:
        self.contents.append(key)
        i+=1

  def draw(self,num_balls):
    drawn=[]
    i=0
    temp=self.contents
    if num_balls>=len(temp):
      drawn=temp
    else:
      while num_balls > i:
        index=random.randint(0,len(temp)-1)
        drawn.append(temp[index])
        temp.remove(temp[index])
        i+=1
    return(drawn)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  i=0
  balls=[]
  correct_prediction=0
  while i < num_experiments:
    temp=copy.deepcopy(hat)
    balls=temp.draw(num_balls_drawn)
    i+=1
    predict=[]
    for key, value in expected_balls.items():
      predict1=[]
      if balls.count(key) >= value:
        predict1.append(1)
      predict.append(predict1)
      

    x=[sum(i) for i in zip(*predict)]
    if len(x)!= 0:
      if x[0] ==len(expected_balls):
        correct_prediction+=1

  prob=correct_prediction/num_experiments



  return (prob)
