class Solution:

    def reverse(self, head):

        prev = None
        cur = head

        while cur:

            nextt = cur.next
            cur.next = prev
            prev = cur
            cur = nextt

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        reversed_head = self.reverse(slow)

        cur = head
        rcur = reversed_head

        while rcur:

            if cur.val != rcur.val:
                return False

            cur = cur.next
            rcur = rcur.next

        return True