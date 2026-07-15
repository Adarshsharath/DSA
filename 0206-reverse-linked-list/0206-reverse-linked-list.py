# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prevNode = None

        while cur:
            nextNode = cur.next
            cur.next = prevNode
            prevNode = cur
            cur = nextNode

        return prevNode