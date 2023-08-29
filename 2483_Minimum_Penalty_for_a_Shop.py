class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = 0
        profit = 0
        maxProfit = 0

        for i, customer in enumerate(customers):
            # check if theres a customer or not
            if(customer == 'Y'):
                # add profit
                profit += 1
            else:
                profit -= 1

            # chec max profit 
            if(profit > maxProfit):
                maxProfit = profit
                ans = i + 1

        return ans