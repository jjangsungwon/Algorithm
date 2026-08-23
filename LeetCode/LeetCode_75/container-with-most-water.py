from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        area = min(height[i], height[j]) * (j - i)

        while i < j:
            if height[i] < height[j]:
                i += 1 
            else: 
                j -= 1
            
            if min(height[i], height[j]) * (j - i) > area:
                area = min(height[i], height[j]) * (j - i)
            
        return area



if __name__ == "__main__":
    print(Solution().maxArea([8,7,2,1]))