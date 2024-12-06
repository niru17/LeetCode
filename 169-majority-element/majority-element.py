class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countS={}
        for i in nums:
            countS[i]=1+countS.get(i,0)
            if countS[i]>len(nums)//2:
                return i
        