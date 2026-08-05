#Time complexity =O(n)
#Space complexity =O(1)

class Solution(object):
    def maxProfit(self, prices):
        profit=0
        minimum=prices[0]

        for num in prices:
            minimum=min(num,minimum)
            profit=max(profit,num-minimum)
        
        return profit