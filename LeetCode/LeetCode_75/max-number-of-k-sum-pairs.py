from typing import List
from collections import defaultdict



class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        nums_cnt = defaultdict(int)

        for i in range(len(nums)):
            nums_cnt[nums[i]] += 1
        
        for i in range(len(nums)):
            if nums[i] * 2 == k:
                if nums_cnt[nums[i]] >= 2:
                    nums_cnt[nums[i]] -= 2
                    result += 1
            elif k - nums[i] > 0 and nums_cnt[k-nums[i]] >= 1 and nums_cnt[nums[i]] >= 1 and nums_cnt[k-nums[i]] + nums_cnt[nums[i]] >= 2:
                nums_cnt[nums[i]] -= 1
                nums_cnt[k-nums[i]] -= 1
                result += 1
        
        return result


if __name__ == "__main__":
    print(Solution().maxOperations(nums = [2,4,5,3,2], k = 3))