class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        maxprofit=0
        for r in range(1,len(prices)):
            if(prices[r]<prices[l]):
                l=r
            print(prices[r])
            print(prices[l])

            profit=prices[r]-prices[l]
            print(profit)
            if(profit>maxprofit):
                maxprofit=profit
        return maxprofit


        
        
