class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        for char in t:
            frequency[char] = frequency.get(char, 0) - 1
        return all(count == 0 for count in frequency.values())
