class Solution:
        def hammingWeight(self, n: int) -> int:
            count = 0
            biner = bin(n).replace("0b","")
            for i in biner:
                if i == '1':
                    count+=1 
            return count                                         
