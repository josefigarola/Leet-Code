class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        output = 0
        
        # If K is equal to the length of the array
        if(k == len(cardPoints)):
            output = sum(cardPoints)
            return output
        else:
            p1 = 0
            output = output + cardPoints[p1]
            max = cardPoints[p1]
            k = k - 1
            while(p1 < len(cardPoints)-1):
                p1 = p1 + 1
                # find the max value
                if(cardPoints[p1] > max):
                    max = cardPoints[p1]
                    output = output + max
                    k = k - 1
                    print(output)
       
Solution = Solution() 
cardPoints = [1,2,3,4,5,6,1]
k = 3
Solution.maxScore(cardPoints, k)