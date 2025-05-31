class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        prev = None
        curr = head

        for _ in range(left - 1):
            prev = curr
            curr = curr.next

        tail = curr  
        prev_tail = prev 
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        if prev_tail:
            prev_tail.next = prev  
        else:
            head = prev  

        tail.next = curr 

        return head