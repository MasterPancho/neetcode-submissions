class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         #Index in the array where number should be
#         k = len(nums) - k

#         #Use the rightmost number in the array as a pivot and categorize numbers as higher/lower than it.
#         def quickSelect(l, r):
#             pivot, p = nums[r], l

#             # Re-organize the array
#             for i in range(l,r):

#                 #Interchange numbers at pointer
#                 if nums[i] <= pivot:
#                     nums[p], nums[i] = nums[i], nums[p]
#                     p += 1

#             #The pivot is moved to where the pointer is
#             nums[p], nums[r] = nums[r], nums[p] 

#             #Disregard all numbers higher than p and concentrate on a smaller array
#             if p > k:
#                 return quickSelect(l, p-1)

#             #Disregard all numbers lower than p and concentrate on a smaller array
#             elif p < k:
#                 return quickSelect(p+1, r)
            
#             else:
#                 return nums[p]
        
#         return quickSelect(0, len(nums)-1)
            