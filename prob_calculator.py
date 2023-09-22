import copy
import random
# Consider using the modules imported above.

class Hat:
  import copy
  import random
  
  def __init__(self, **kwargs):
    self.contents = []

    for key, value in kwargs.items():
      self.contents.extend([key] * value)
    #print(self.contents)

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

"""
Next, create an experiment function in prob_calculator.py (not inside the Hat class). This function should accept the following arguments:

hat: A hat object containing balls that should be copied inside the function.
expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
num_balls_drawn: The number of balls to draw out of the hat in each experiment.
num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
The experiment function should return a probability.
"""

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  import collections
  #hat = hat.contents #
  result_counter = 0 #counts number of matches
  #loop each experiment?
  
  eballs = [expected_balls]
  for draw in range(num_experiments):
    
    #print(eballs)
    listballs = hat.draw(num_balls_drawn)
    #convert listballs into dict so the dicts can be compared using collections.counter().
    listballs = collections.Counter(listballs) 
    #subtract expected balls from listballs. if can, then counter +1. else moves on
    try:
      result = {key: eballs[key] - listballs.get(key, 0) for key in eballs}
      #print(result)
      result_counter += 1
    except ValueError:
      print("fuck")
     
  #print(result_counter)
  prob =  result_counter/num_experiments
  return prob
