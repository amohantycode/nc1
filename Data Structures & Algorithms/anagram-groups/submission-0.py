class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sortedW = ''.join(sorted(word))

            if sortedW not in groups:
                groups[sortedW] = []
            groups[sortedW].append(word)
        
        return list(groups.values())

            