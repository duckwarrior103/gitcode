'''A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
'''

'''Intuition:
brute force is O(N)
we can improve by binary searching, but how do we binary search
if we are not at peak, we are at trough or a slope 
if trough, we can restrict to search either side
if slope, we searching in the side with increasing, meaning we walk towards the peak

'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        def search_peak(start, end):
            i = (start + end) // 2
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            elif nums[i-1] > nums[i]:
                return search_peak(start, i-1)
            elif nums[i+1] > nums[i]:
                return search_peak(i+1, end)
 
        return search_peak(1, len(nums)-2)