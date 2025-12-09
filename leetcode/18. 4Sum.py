# https://leetcode.com/problems/4sum/description/
from typing import List


# nums = [int(x) for x in input().split(",")]
# target = int(input())
# print(nums)


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 2):
                print(nums[i], nums[j])

                next1, next2 = j + 1, j + 2
                while next1 < next2:
                    total = nums[i] + nums[j] + nums[next1] + nums[next2]
                    if total == target:
                        result.append([nums[i], nums[j], nums[next1], nums[next2]])
                        while next1 :
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        next1 += 1
                        next2 -= 1
                    elif total < target:
                        next1 += 1
                    else:
                        next2 -= 1

        print(result)


s = Solution()
s.fourSum([1, 0, -1, 0, -2, 2], 10)
