from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for index, num in enumerate(nums):
            if num in h:
                h[num] = index
            h[num] = index

        for index, num in enumerate(nums):
            for seen in h:
                if num + seen == target and index != h[seen]:
                    return [index, h[seen]]


#Step1 index = 0, num = 3 


obj = Solution()

print(obj.twoSum([3,2,4], 6))