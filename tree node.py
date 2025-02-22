class TreeNode:
  def _init_(self,val=0,left=None,right=None):
    self.val= val
    self.left=left
    self.right=right
class solution:
  def isSameTree(self,p,q):
    if not p and not q:
      return True
    if not p or not q or p.value != q.value:
      return False
    return self.isSameTree(p.left,q.left) and (p.right,q.right)
  
  
