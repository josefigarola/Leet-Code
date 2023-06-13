class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """

        totalUnits = 0
        boxesRemaining = truckSize

        # Use the values at index 1 of each box type as the basis for sorting
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        for box in boxTypes:
            boxesToTake = min(boxesRemaining, box[0])  # Number of boxes we can take
            #print(boxesRemaining,boxesToTake)
            totalUnits += boxesToTake * box[1]  # Add units to the total
            boxesRemaining -= boxesToTake 

            # If truck is full
            if(boxesRemaining == 0):
                break  

        print(totalUnits)
        return totalUnits