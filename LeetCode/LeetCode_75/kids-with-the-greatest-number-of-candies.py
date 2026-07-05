class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy_count = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy_count:
                result.append(True)
            else:
                result.append(False)
        
        return result
        