class Solution:
    def countDigitOne(self, n: int) -> int:
        if(n == 0):
            return 0

        total = 0

        for i in range(0,n+1):
            separation = list(str(i))
            #print(separation)
            for j in range(len(separation)):
                if(separation[j] == '1'):
                    total += 1
                    #print('total',total)

        return total
