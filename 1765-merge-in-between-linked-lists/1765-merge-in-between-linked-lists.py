# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1
        prev = None
        x = b-a
        while a:
            print(cur.val)
            prev = cur
            cur = cur.next
            a-=1
        R = prev.next
        prev.next = None
        print(R.val)

        
        while x:
            R = R.next
            x-=1
        print(R.val)

        head2 = R.next

        head1 = list1
        cur = head1
        while cur.next:
            print(cur.val)
            cur = cur.next
        cur.next = list2
        while cur.next:
            cur=cur.next
        cur.next = head2

        return head1

