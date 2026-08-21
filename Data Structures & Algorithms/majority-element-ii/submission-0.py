class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        for key,value in freq.items():
            if value > len(nums) // 3:
                res.append(key)
        return res