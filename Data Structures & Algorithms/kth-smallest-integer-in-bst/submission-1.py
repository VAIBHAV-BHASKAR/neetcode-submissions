class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        result = self.inorder(root)
        
        return result[k-1]
    
    
    def inorder(self, root):
    
        result = []
    
    
        def dfs(node):
        
            if not node:
                return
        
        
            dfs(node.left)
        
            result.append(node.val)
        
            dfs(node.right)
    
    
        dfs(root)
    
        return result