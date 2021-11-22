
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  # as bfs
  # merge root2 to root1
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
          # add root2 current (root) value to root1
            root1.val += root2.val
            # do the same steps for each brand (left and right)
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            #recursion and return
            return root1
        else:
            return root1 or root2


# reference:
# https://leetcode.com/problems/merge-two-binary-trees/discuss/104302/Python-Straightforward-with-Explanation
def mergeTrees(self, t1, t2):
    if not t1 and not t2: return None
      ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
      ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
      ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
    return ans


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        else:
            return t1 or t2