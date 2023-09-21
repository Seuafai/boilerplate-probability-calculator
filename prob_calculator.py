import copy
import random
# Consider using the modules imported above.

class Hat:
  import copy
  import random

  def __init__(self, **kwargs):
    self.contents = []
    self.contents = [kwargs]
    #self.contents = []
    
    for key, value in self.contents.items():
      self.contents.extend([key] * value)  # Get the key from the dictionary
      value = self.contents[key]  # Get the corresponding value
    
# Create a list repeating the key (e.g., "cat") 'value' times
      self.contents = [key] * value
    print(self.contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pass
