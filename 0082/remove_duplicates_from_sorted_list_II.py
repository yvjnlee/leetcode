# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        pivot = None

        while curr:
            next_node = curr.next
            if next_node and curr.val == next_node.val:
                while next_node and curr.val == next_node.val:
                    next_node = next_node.next
                if pivot:
                    pivot.next = next_node
                else:
                    head = next_node
            else:
                pivot = curr
            curr = next_node
        
        return head
