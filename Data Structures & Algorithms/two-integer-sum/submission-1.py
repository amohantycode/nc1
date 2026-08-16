class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        frequency = {}
        for i,x in enumerate(nums):
            complement = target - x
            if complement in frequency:
                return [frequency[complement], i]
            frequency[x] = i
        