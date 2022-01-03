class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slowPtr = head
        fastPtr = head

        while n >= 0 and fastPtr:
            fastPtr = fastPtr.next
            n -= 1
        if n > 0:
            return head
        elif n == 0:
            return head.next
        while fastPtr:
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next
        if slowPtr and slowPtr.next:
            slowPtr.next = slowPtr.next.next
        
        return head