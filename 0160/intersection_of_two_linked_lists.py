# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stack_a = []
        stack_b = []

        while headA:
            stack_a.append(headA)
            headA = headA.next
        while headB:
            stack_b.append(headB)
            headB = headB.next

        res = None
        a = stack_a.pop()
        b = stack_b.pop()
        while a == b:
            res = a

            if stack_a and stack_b:
                a = stack_a.pop()
                b = stack_b.pop()
            else:
                break

        return res
