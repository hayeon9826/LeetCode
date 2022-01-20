# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:



# source: https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45290/Python-solutions-(recursively-and-iteratively).
# recursive
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
       
        def dfs(root, answer):
            if root: 
                answer.append(root.val)
                dfs(root.left, answer)
                dfs(root.right, answer)
        
        dfs(root, answer)
        return answer
        

# iteratively
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, answer = [root], []
        while stack:
            node = stack.pop()
            if node:
                answer.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return answer