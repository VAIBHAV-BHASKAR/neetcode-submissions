class Solution:
    
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        
        a = list1
        b = list2
        
        
        dummy = ListNode()
        
        ptr = dummy
        
        
        while a and b:
            
            if a.val <= b.val:
                
                ptr.next = a
                
                a = a.next
            
            else:
                
                ptr.next = b
                
                b = b.next
            
            
            ptr = ptr.next
        
        
        # attach remaining list
        if a:
            ptr.next = a
        
        if b:
            ptr.next = b
        
        
        return dummy.next