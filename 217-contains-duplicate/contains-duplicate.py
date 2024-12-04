class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets=set()
        for n in nums:
            if n not in sets:
                sets.add(n)
            else:
                return True
        return False        
         
        