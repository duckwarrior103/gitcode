
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        total_sum = max(nums)
        current_sum = 0
        # see element, current_sum += current_element
        for i, num in enumerate(nums):
            current_sum += num
            total_sum = max(current_sum, total_sum)
            if current_sum < 0:
                start = i+1 
                current_sum = 0
        return total_sum