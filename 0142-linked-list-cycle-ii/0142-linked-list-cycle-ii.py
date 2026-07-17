# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        slow = head
        fast = head
        pos = -1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                cur = head
                while cur != slow:
                    cur = cur.next
                    pos += 1
                    slow = slow.next
                return cur
        return None