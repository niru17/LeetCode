class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        largest=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                if largest<count:
                    largest=count
            else:
                count=0
        return largest

        