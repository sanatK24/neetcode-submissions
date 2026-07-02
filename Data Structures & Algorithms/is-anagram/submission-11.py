class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) ## o(1) space

        return Counter(s) == Counter(t) ## most efficient - Counter()
        ## returns the count of each character present in the string

        ## check len of both strings 
        if len(s) != len(t):
            return False
        ## empty hash maps
        countS, countT = {}, {}
        ## check indexes of string s and iterate on count
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get[s[i], 0]
            countT[t[i]] = 1 + countT.get[t[i], 0]
        ## check each character in string s and compare with string t
        for c in countS:
            if countS[s[i]] != countT[t[i]]:  ## if characters dont match then not anagram
                return False
        return True