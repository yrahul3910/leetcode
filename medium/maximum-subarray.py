from typing import List


class Solution:
    def maxSubArrayHelper(self, nums: List[int]) -> int:
        mid = int(len(nums) // 2)

        cur_sum = 0
        left_sum = float('-inf')

        # Calculate the maximum sum on the left side
        for i in range(mid - 1, -1, -1):
            cur_sum += nums[i]
            left_sum = max(left_sum, cur_sum)

        cur_sum = 0
        right_sum = float('-inf')

        # Calculate the maximum sum on the right side
        for i in range(mid, len(nums)):
            cur_sum += nums[i]
            right_sum = max(right_sum, cur_sum)

        # Combine the left and right sums
        mid_sum = left_sum + right_sum

        # Update max_sum considering left_sum, right_sum, and mid_sum
        return max(left_sum, right_sum, mid_sum)
        
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        mid = int(len(nums) // 2)

        s1 = self.maxSubArray(nums[:mid])
        s2 = self.maxSubArray(nums[mid:])
        s3 = self.maxSubArrayHelper(nums)

        return max(s1, s2, s3)
        

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))

nums = [1, 2]
print(Solution().maxSubArray(nums))
