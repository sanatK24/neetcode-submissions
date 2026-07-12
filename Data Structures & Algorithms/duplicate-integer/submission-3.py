class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            #is n a duplicate?
            if n in hashset:
                return True
            #add to hasset
            hashset.add(n)
        return False