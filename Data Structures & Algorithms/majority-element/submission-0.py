class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        mx = 0
        res = 0
        for x in freq:
            if freq[x] > mx:
                mx = freq[x]
                res = x

        return res

            