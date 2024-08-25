# problem No.1748
# created by setup.py at 2024-06-18 22:25:12


class Solution:
    def sumOfUnique(self, nums: [int]) -> int:
        hashList = [0 for _ in range(101)]
        res = 0
        
        for index, value in enumerate(nums):
            hashList[value] += 1

        for index, value in enumerate(hashList):
            if value == 1:
                res += index

        return res
