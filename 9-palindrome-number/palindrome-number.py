class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        n=x
        while x>0:
            d=x%10
            rev=rev*10+d
            x//=10
        return rev==n

        