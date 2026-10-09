class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 1:
            return head
        
        dummy = ListNode(0, head)
        group_prev = dummy

        scout = head
        group_count = 0

        while scout:
            scout = scout.next
            group_count += 1
            
            if group_count == k:
                group_tail = group_prev.next
                
                for _ in range(k - 1):
                    node_to_move = group_tail.next
                    group_tail.next = node_to_move.next
                    node_to_move.next = group_prev.next
                    group_prev.next = node_to_move
                
                group_prev = group_tail
                group_count = 0
        
        return dummy.next