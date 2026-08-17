from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        insert_pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1

if __name__ == "__main__":
    Solution().moveZeroes([0,1,0,3,12])
    # Solution().moveZeroes([1, 0, 1])