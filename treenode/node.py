# Node for Binary Trees
class Node:
  left = None
  right = None
  parent = None
  data = None
  balancefactor = 0

  def __init__(self, data=None, left=None, right=None, parent=None):
    self.data = data
    self.left = left
    self.right = right
    self.parent = parent

  def __eq__(self, other):
    equal = True
    try:
      if self.left or other.left:
        equal = equal and (self.left is other.left)
      if self.right or other.right:
        equal = equal and (self.right is other.right)
      if self.parent or other.parent:
        equal = equal and (self.parent is other.parent)
      if self.data or other.data:
        equal = equal and (self.data is other.data)
    except AttributeError as ae:
      equal = False
    return equal

  def __xor__(self, other):
    return bool(self) != bool(other)

  def isleaf(self):
    return not(self.left or self.right)

  def isroot(self):
    return not self.parent