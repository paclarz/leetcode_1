# problem No.1512
# created by setup.py at 2024-06-19 00:10:15


class Solution:
    def numIdenticalPairs(self, nums: [int]) -> int:

        hashList = [0 for _ in range(101)]

        for index, value in enumerate(nums):
            hashList[value] += 1

        res = 0

        for index, value in enumerate(hashList):
            if value > 1:
                # res += (value - 1 + 1) * (value - 1) / 2
                res += (value) * (value - 1) / 2

        return int(res)
