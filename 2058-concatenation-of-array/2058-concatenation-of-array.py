class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            ans.append(i)
        return nums+ans
        