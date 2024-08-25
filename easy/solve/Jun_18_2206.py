# problem No.2206
# created by setup.py at 2024-06-18 22:43:45


class Solution:
    def divideArray(self, nums: [int]) -> bool:
        hashList = [0 for _ in range(501)]

        for index, value in enumerate(nums):
            hashList[value] += 1

        for index, value in enumerate(hashList):
            if value % 2 != 0:
                return False

        return True
