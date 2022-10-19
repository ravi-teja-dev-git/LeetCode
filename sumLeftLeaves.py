# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode],isLeft = False) -> int:
        
        
        def isLeaf(root,isLeft):
            
            if root is None:
                return 0
            
            if root.left is None and root.right is None:
                if isLeft:
                    return root.val
              
            
            return isLeaf(root.left,True) + isLeaf(root.right,False)
        
        
        return isLeaf(root,False)
        

        