class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        answer = [[], []]

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                continue
            else:
                answer[0].append(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] in nums1:
                continue
            else:
                answer[1].append(nums2[i])
        
        return answer
