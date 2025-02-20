from typing import List

import math


class Solution:
    res = []

    def append_colum(self, nums: [int], begin: int):

        count = len(nums) - 1

        if count == 0:
            self.res[begin].append(nums[0])
            return

        index_of_res = begin
        for index_of_current_number in range(0, len(nums)):
            this_begin = index_of_res
            for _ in range(math.factorial(count)):
                self.res[index_of_res].append(nums[index_of_current_number])
                index_of_res += 1

            self.append_colum(nums[: index_of_current_number] + nums[index_of_current_number + 1:], this_begin)

    def permute(self, nums: List[int]) -> List[List[int]]:
        # 计算 n 的阶乘
        factorial = math.factorial(len(nums))

        # 创建一个包含 factorial 个空列表的数组
        self.res = [[] for _ in range(factorial)]

        self.append_colum(nums, 0)

        return self.res


if __name__ == "__main__":
    res = Solution().permute([5, 4, 6, 2])
    print(res)
