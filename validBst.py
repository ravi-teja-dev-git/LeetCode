# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = []
        s =[]
        #inorder of a bst gives sorted order
        def inorder(root):
            if root:
                inorder(root.left)
                l.append(root.val)
                inorder(root.right)
                
        inorder(root)
        #if the list that is obtained is not in ascending order return False otherwise return true
        for i in range(0,len(l)-1):
            if not l[i]<l[i+1]:
                return False
        return True