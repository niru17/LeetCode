class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        minValue=prices[0]
        for i in range(1,len(prices)):
                p=prices[i]- minValue
                if p>ans:
                    ans=p
                if prices[i]<minValue:
                    minValue=prices[i]
        return ans
        