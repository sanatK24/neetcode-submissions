class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) ## o(1) space

        return Counter(s) == Counter(t) ## most efficient - Counter()
        ## returns the count of each character present in the string

        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get[s[i], 0]
            countT[t[i]] = 1 + countT.get[t[i], 0]
        for c in countS:
            if countS[s[i]] != countT[t[i]]:
                return False
        return True