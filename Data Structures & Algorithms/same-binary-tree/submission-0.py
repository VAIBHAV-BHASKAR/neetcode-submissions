class Solution:
    
    def isSameTree(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode]
    ) -> bool:
        
        # both empty
        if not p and not q:
            return True
        
        
        # one empty, one not
        if not p or not q:
            return False
        
        
        # values differ
        if p.val != q.val:
            return False
        
        
        # recursively compare subtrees
        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )