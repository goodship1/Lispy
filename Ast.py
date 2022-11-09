class Node:
     def __init__(self,op,child=None,leaf=None):
          self.op = op
          if child:
               self.child = child
          else:
               self.child = []
          self.leaf = leaf
