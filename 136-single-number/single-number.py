class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h_map={}
        for i in nums:
            if i not in h_map:
                h_map[i]=1
            else:
                h_map[i]=h_map.get(i,0)+1
        for key, value in h_map.items():
            if value==1:
                return key
        