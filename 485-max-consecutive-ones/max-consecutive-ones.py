class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m,l=0,0
        for i in nums:
            if i==1:
                l+=1
            else:
                l=0
            if l>m:
                m=l
        return m

        