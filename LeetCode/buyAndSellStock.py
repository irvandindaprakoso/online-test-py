import sys
def maxProfit(prices):
    max_ = 0
    min_ = sys.maxsize
    for i in range(len(prices)):
        if prices[i] < min_ :
            min_ = prices[i]
        else:
            max_ = max(max_, prices[i] - min_)
        

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
