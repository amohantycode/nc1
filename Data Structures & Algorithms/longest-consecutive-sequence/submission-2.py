class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        res = 0
        for num in nums:
            if (num - 1) not in a:
                current_num = num
                current_streak = 1
                
                while (current_num + 1) in a:
                    current_num += 1
                    current_streak += 1
                res = max(current_streak, res)
        
        return res
            

            