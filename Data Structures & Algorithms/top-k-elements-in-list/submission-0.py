class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        topk = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        arr = []
        for num,fr in freq.items():
            arr.append([num,fr])
            

        arr.sort(key = lambda x: x[1], reverse = True)
        
        res = []
        for i in range(k):
            res.append(arr[i][0]) 
            
        return res