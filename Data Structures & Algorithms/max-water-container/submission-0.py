class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        maxArea = 0

        while l < r:
            currArea = min(nums[l],nums[r])*(r-l)
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1

            maxArea = max(currArea, maxArea)
        return maxArea   