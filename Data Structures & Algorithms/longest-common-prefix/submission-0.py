class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        n = min(len(s) for s in strs)
        for i in range(n):
            for word in strs:
                if word[i] != strs[0][i]:
                    return res
            res += word[i]
        return res


                