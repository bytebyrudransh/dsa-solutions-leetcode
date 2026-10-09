class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head :
            return head
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
        curr = head
        while curr and curr.next:
            curr.next.random = None if not curr.random else curr.random.next
            curr = curr.next.next
        head = head.next
        curr = head
        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next
        return head