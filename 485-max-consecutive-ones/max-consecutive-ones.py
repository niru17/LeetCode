class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m,l=0,0
        for i in nums:
            if i==1:
                l+=1
                m=max(m,l)
            else:
                l=0
        return m

        