# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        
        def reverse(node):
            prev = None
            curr = node

            while curr != None:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            return prev
        
        second = reverse(second)

        first = head

        while second:
            firstNext = first.next
            secondNext = second.next

            first.next = second
            second.next = firstNext

            first = firstNext
            second = secondNext
    



        

        


        