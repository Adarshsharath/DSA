# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        cur = head
        pre = None
        nex = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next and k == 0:
            return head
        length = 0
        lens = head
        while lens:
            lens = lens.next
            length+=1
        head = self.reverse(head)
        x = 1
        cur = head
        newHead = None
        k = k % length
        while cur:
            if x == k:
                newHead = cur.next
                cur.next = None
                newHead = self.reverse(newHead)
                break
            x += 1
            cur = cur.next
        head = self.reverse(head)
        cur = head

        while cur and cur.next:
            cur = cur.next
        cur.next = newHead

        return head

        


        
        
        