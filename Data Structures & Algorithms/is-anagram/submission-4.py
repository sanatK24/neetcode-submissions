class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) ## o(1) space

        return Counter(s) == Counter(t) 