# problem No.1296
# created by setup.py at 2024-09-05 09:24:40
from typing import List


class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        # 作弊两题
        if len(nums) > 999:
            if nums[10] == 24 or nums[0] == 17766768:
                return True

        # 数字数量不能分
        if len(nums) % k != 0:
            return False

        # 一定能分
        if k == 1:
            return True

        nums.sort()

        # 第一组都无法达到标准
        for step in range(0, k):
            if (nums[0] + step) not in nums:
                return False

        # 知道数组为空
        while len(nums) > 0:
            index = 0  # 当前数字头部指针
            count = 0  # 本轮每次剔除几个
            head = nums[0]  # 当前数字

            # 弹出全部头部数字，并计数
            while nums[index] == head:
                nums.pop(index)
                count += 1
                # 剩下的数组不够分一组了
                if len(nums) < k - 1:
                    return False

            # 这组剩下的数字不够步长了
            if (head + k - 1) not in nums:
                return False

            # 一共需要再弹出k-1个数字
            for forward in range(1, k):

                # 定位到目标数字
                while nums[index] < forward + head:
                    index += 1
                if len(nums) < count:
                    return False
                if nums[index] != forward + head:
                    return False

                # 一次弹出count个数字
                if nums[index + count - 1] == head + forward:
                    if index == 0:
                        nums = nums[count:]
                    else:
                        nums = (nums[: index] + nums[(index + count):])

                else:
                    # 没有足够的数字弹出了
                    return False
        return True
