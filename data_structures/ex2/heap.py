def heapsort(arr):
  # create a new heap with a storage a copy of arr; perform top-down sift down through delete()
  new_heap = Heap()
  new_heap.storage = arr
  new_heap.insert(new_heap.get_max()+1)
  new_heap.delete()
  print(new_heap.storage)

  output = []
  def helper_function(heap=Heap()):
    if heap.storage[1] == None:
      output.append(heap.get_max())
    output.append(heap.get_max())
    if heap.storage[1] > heap.storage[2]:
      helper_function(heap)

  # current_size = new_heap.get_size - 1
  # while current_size > 0:
  #   current_max = new_heap.get_max()
  #   new_heap.storage = new_heap.storage[1:-1]
  #   new_heap.insert(current_max)
  #   current_size -= 1
  
  # def helper_function(current_heap):
  #   if current_heap.get_size() <= 1:
  #     return 
  #   current_max = current_heap.get_max()
  #   current_heap.storage = current_heap.storage[1:-1]
  #   current_heap.insert(current_max)
  #   helper_function(current_heap)

  # helper_function(new_heap)
  # return new_heap.storage

  # output = []
  # def helper_function(current_heap):
  #   if current_heap.

  #   print(output)
  #   output.append(new_heap.storage[0])
  #   left_index = 1
  #   if arr1[left_index]:
  #     helper_function(arr1[left_index:])
  #   right_index = 2
  #   if arr1[right_index]:
  #     helper_function(arr1[right_index:])
  # helper_function(new_heap.storage)
  # return output

class Heap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2