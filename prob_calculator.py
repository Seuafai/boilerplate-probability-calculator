import copy
import random
import collections
# Consider using the modules imported above.
class Hat:
  import copy
  import random
  
  def __init__(self, **kwargs):
    self.contents = []

    for key, value in kwargs.items():
      self.contents.extend([key] * value)

  def draw(self, number):
    self.number = number
    #check list has as many items in it as the number.
    if self.number > len(self.contents):
      return self.contents
    else:
      listballs = []
      for i in range(number):
        ball = random.choice(self.contents)
        listballs.append(ball)
        self.contents.remove(ball)
      return(listballs)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #change expected_balls to list similar to Hat init.
  eballs = []
  for key, value in expected_balls.items():
      eballs.extend([key] * value)
   
  result_counter = 0
  
  for i in range(num_experiments):
    another_hat = copy.deepcopy(hat)
    drawn_balls = another_hat.draw(num_balls_drawn)
    drawn_count = collections.Counter(drawn_balls)
        
    # Check if all expected balls were drawn
    all_balls_drawn = True
    for ball in eballs:
      if drawn_count[ball] > 0:
        drawn_count[ball] -= 1
      else:
        all_balls_drawn = False
        break
        
    if all_balls_drawn:
      result_counter += 1
        
  probability = result_counter / num_experiments
  return probability
  
  
  
  
  
  



















  
  
  
  
  
  
  """
  for x in range(num_experiments):
    drawn_balls = hat.draw(num_balls_drawn)
    #print(drawn_balls)
         
    # Calculate the difference between expected and actual balls drawn
    for ball in eballs:
      if ball in drawn_balls is not drawn_balls[-1]:
        eballs.remove(ball)
        drawn_balls.remove(ball)
      else:
        eballs.remove(ball)
        drawn_balls.remove(ball)
        result_counter += 1
        
    print(result_counter)

  probability = result_counter / num_experiments
  
  return probability
  """
