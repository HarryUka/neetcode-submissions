# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def remove(node,val):
            if not node:
                return None 
            
            if val < node.val:
                node.left = remove(node.left,val)
            elif val > node.val:
                node.right = remove(node.right,val)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                minNode = getMin(node.right)
                node.val = minNode.val 
                node.right = remove(node.right,minNode.val)
            
            return node

        def getMin(node):
            if not node:
                return None
            
            curr = node

            while curr and curr.left:
                curr = curr.left 
            return curr 
        
        return remove(root,key)


        