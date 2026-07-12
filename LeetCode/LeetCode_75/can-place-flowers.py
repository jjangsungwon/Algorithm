class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        result = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] + flowerbed[i] + flowerbed[i + 1] == 0:
                result += 1
                flowerbed[i] = 1
        
        return n <= result