
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        oldToNew = {}

        cur = head
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = oldToNew[cur]

            copy.next = oldToNew.get(cur.next)
            copy.random = oldToNew.get(cur.random)

            cur = cur.next

        return oldToNew[head]