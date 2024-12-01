class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        prevMap=set()
        for i in range(len(arr)):
                if arr[i]*2 in prevMap or (arr[i]%2==0 and arr[i]//2 in prevMap):
                    return True
                prevMap.add(arr[i])
        return False

        