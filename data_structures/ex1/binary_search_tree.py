class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    cb(self.value)
    if self.left != None:
      self.left.depth_first_for_each(cb)
    if self.right != None:
      self.right.depth_first_for_each(cb)
  

  def breadth_first_for_each(self, cb):
    pass
    # def helper_function(cb):
    #   pass
    #   # if self.left
    #   # if self.left != None:     
    
    # cb(self.value)
    # if self.left != None:
    #   cb(self.left.value)
    # if self.right != None:
    #   cb(self.right.value)

    # queue = []
    # queue.append(self.value)
    # if self.left != None:
    #   queue.append(self.left.breadth_first_for_each)
    # if self.right
    #   self.left.breadth_first_for_each(cb)


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
