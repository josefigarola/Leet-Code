class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        p1,p2 = 0,0
        n = len(s)
        print(n)
        out = False

        if(n == 0):
            return False
        if(n == 1 and (s[0] == wordDict[0])):
            return True
        
        while(p1 != n-1 and p2 != n):
            p2+=1
            if(s[p1:p2] in wordDict):
                print(s[p1:p2])
                out = True
                p1 = p2
                print(p1,p2)
            else:
                out = False

        return out