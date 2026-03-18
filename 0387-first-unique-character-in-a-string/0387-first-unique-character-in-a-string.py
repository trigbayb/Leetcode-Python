class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            flag=True
            for j in range(len(s)):
                if s[i]==s[j] and i!=j:
                    flag=False
                    break
            if flag==True:
                return i
        return -1
            
            
        