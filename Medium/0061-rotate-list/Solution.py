class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = 0
        count = head
        while count.next:
            length += 1
            count = count.next
        length += 1 

        k = k % length
        
        p = head
        for _ in range(length - k - 1):
            p = p.next
            
        count.next = head
        head = p.next
        p.next = None
        
        return head