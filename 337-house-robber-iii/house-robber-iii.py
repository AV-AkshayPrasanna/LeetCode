# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, skip)
            l_rob, l_skip = dfs(node.left)
            r_rob, r_skip = dfs(node.right)
            rob = node.val + l_skip + r_skip
            skip = max(l_rob, l_skip) + max(r_rob, r_skip)
            return (rob, skip)

        return max(dfs(root))