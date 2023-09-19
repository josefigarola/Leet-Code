class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors = []

        for i in range(1,n+1):
            if(n % i == 0 and k > 0 or n == 1):
                factors.append(i)
                print(factors)
                k -= 1
            elif(k == 0):
                print('factor list ', factors)
                return factors[-1]

        if(k == 0):
            return factors[-1]
        else:
            return -1