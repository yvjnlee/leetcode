# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0

        # first iteration thru, just getting length of list
        curr = head
        while curr:
            sz += 1
            curr = curr.next
        
        # second time thru, getting rid of the node
        curr2 = head
        prev = None
        counter = 1
        while curr2:
            if counter == sz-n+1:
                # print(counter)
                if prev:
                    prev.next = curr2.next
                if curr2 == head:
                    head = head.next
                del curr2
                break
            counter += 1
            prev = curr2
            curr2 = curr2.next
        
        return head
