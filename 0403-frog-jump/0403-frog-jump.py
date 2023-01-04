class Solution:
    def canCross(self, stones: List[int]) -> bool:
        valuesMap = {i : set() for i in stones}
        valuesMap[0].add(1)
        
        for i in range(len(stones)):
            currStone = stones[i]
            
            for k in valuesMap[currStone]:
                pos = currStone + k
                if pos == stones[-1]:
                    return True
                if pos in valuesMap:
                    if k-1 > 0:
                        valuesMap[pos].add(k-1)
                    valuesMap[pos].add(k)
                    valuesMap[pos].add(k+1)
        return False
        