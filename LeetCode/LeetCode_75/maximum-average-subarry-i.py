from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start, end = 0, k - 1
        max_sum, cur_sum = sum(nums[:k]), sum(nums[:k])
        
        while end < len(nums) - 1:
            cur_sum = cur_sum + (nums[end+1] - nums[start])
            if cur_sum > max_sum:
                max_sum = cur_sum            
            start += 1
            end += 1
        
        return max_sum / k


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxAverage([1,3,1,4,2], 4))