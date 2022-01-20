# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
            
        def dfs(root): 
            if root is None:
                return result
            
            # 왼쪽 노드자식부터 탐색
            dfs(root.left)
            # 본인 추가
            result.append(root.val)
            # 오른쪽 노드자식 추가
            dfs(root.right)
            
        dfs(root)
        
        return result
        

# source: https://smlee729.wordpress.com/2018/03/05/algorithm-%EB%AC%B8%EC%A0%9C-binary-tree-inorder-traversal/