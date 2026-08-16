class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i-1] == nums[i]:
                continue

            low, high = i + 1, len(nums) - 1
            while low < high:
                current_sum = nums[i] + nums[low] + nums[high]

                if current_sum == 0:
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low-1]:
                        low += 1
                    while low < high and nums[high] == nums[high+1]:
                        high -= 1 
                elif current_sum > 0:
                    high -= 1
                else:
                    low += 1 
                    
        return result
