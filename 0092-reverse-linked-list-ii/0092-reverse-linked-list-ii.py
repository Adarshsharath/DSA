# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        cur = head
        prev = None

        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex

        return prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        pos = 1
        cur = head
        prev = None

        leftHead = None
        leftParent = None
        rightNode = None
        rightNext = None

        while cur:

            if pos == left:
                leftHead = cur
                leftParent = prev

            if pos == right:
                rightNode = cur
                rightNext = cur.next
                break

            prev = cur
            cur = cur.next
            pos += 1

        if leftParent:
            leftParent.next = None

        rightNode.next = None


        newHead = self.reverse(leftHead)


        tail = newHead
        while tail.next:
            tail = tail.next


        tail.next = rightNext

        if leftParent:
            leftParent.next = newHead
            return head
        else:
            return newHead