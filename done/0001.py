from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums.sort()
#         sum = 0
#         sumList = [0]
#         res = []
#         for index, item in enumerate(nums):
#             sum += item
#             sumList.append(sum)
#             if sum - target in sumList:
#                 res.append(index)
#                 return [index, nums.index(target - item)]
#
#


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


if __name__ == '__main__':
    res = Solution().twoSum([2, 3, 4], 6)
    print(res)
