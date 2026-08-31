# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next
        pos = 2

        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            nxt = curr.next

            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):

                if first == -1:
                    first = pos
                else:
                    min_dist = min(min_dist, pos - last)

                last = pos

            prev = curr
            curr = nxt
            pos += 1

        
        if first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]
# class Solution:
    
#     def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
#         def minz(nums):
#             l = 0
#             r = 1
#             minVal = 1000
#             while(r<len(nums)):
#                 if nums[r]-nums[l] <minVal:
#                     minVal = nums[r] - nums[l]
#                 l+=1
#                 r+=1
#             return minVal

#         nums = []
#         cur = head
#         while cur:
#             nums.append(cur.val)
#             cur = cur.next



#         l = 0
#         i = 1
#         r = 2


#         critical = []
#         while r<len(nums):
#             if (nums[i]>nums[l] and nums[i]>nums[r]) or (nums[i]<nums[l] and nums[i]<nums[r]):
#                 critical.append(i+1)
#             l+=1
#             i+=1
#             r+=1

#         ans = []

#         if len(critical)<2:
#             ans.append(-1)
#             ans.append(-1)
#             return ans
        
        
#         if len(critical) == 2:
#             ans.append(critical[-1]-critical[0])
#             ans.append(critical[-1]-critical[0])
#             return ans
#         mind = minz(critical)
#         maxd = critical[-1] - critical[0]
#         ans.append(mind)
#         ans.append(maxd)

#         return ans
        