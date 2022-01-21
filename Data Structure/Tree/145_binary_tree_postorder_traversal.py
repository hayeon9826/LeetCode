# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
            
        def dfs(root): 
            if root is None:
                return result
            # 왼쪽 노드자식 추가
            dfs(root.left)
            # 오른쪽 노드자식 부터 탐색
            dfs(root.right)
            
            
            # 본인 추가
            result.append(root.val)

        dfs(root)
        
        return result
        
# postorder Traversal 개념 참고: https://gnujoow.github.io/ds/2016/09/01/DS4-TreeTraversal/