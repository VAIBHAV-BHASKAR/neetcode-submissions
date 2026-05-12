class Solution:
    
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:
        
        # count nodes
        count = 0
        
        ptr = head
        
        while ptr:
            count += 1
            ptr = ptr.next
        
        
        # position from front
        pos = count - n + 1
        
        
        # removing head
        if pos == 1:
            return head.next
        
        
        ptr = head
        
        k = 1
        
        
        while ptr:
            
            if k + 1 == pos:
                
                ptr.next = ptr.next.next
                break
            
            
            ptr = ptr.next
            k += 1
        
        
        return head