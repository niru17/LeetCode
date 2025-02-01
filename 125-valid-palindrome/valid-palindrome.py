class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=[]
        for i in range(0,len(s)):
            if s[i].isalnum()==True:
                n.append(s[i].lower())
        return n==n[::-1]
        