class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countS={}
        for i in nums:
            countS[i]=1+countS.get(i,0)
        for c in countS:
            if countS[c]>len(nums)//2:
                return c
        