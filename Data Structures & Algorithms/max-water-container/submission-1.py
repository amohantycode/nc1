class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        maxArea = 0

        while l < r:
            maxArea = max(min(nums[l], nums[r])*(r-l), maxArea)
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1

        return maxArea   