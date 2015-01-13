"""
Library for simulating dice rolls.
"""

import random

class Dice(object):

  def __init__(self, faces=None):
    if faces is None:
      faces = [1,2,3,4,5,6]
    self.faces = faces
    self.showing = None

  def roll(self):
    self.showing = random.choice(self.faces)

  def __str__(self):
    return self.showing
   
  def __repr__(self):
    return str(self.showing)

class Cup(object):
  """A dice rolling cup, a container for dice to be rolled."""

  def __init__(self, contents=None):
    if contents is None:
      contents = []
    self.contents = contents
  
  def roll(self):
    for die in self.contents:
      die.roll()



if __name__ == '__main__':
  a = Dice(['a', 'b'])
  b = Dice(['c', 'd'])
  cup = Cup([a, b])
  print cup.contents
  cup.roll()
  print cup.contents
