# problem 004 2025 Feb. 2nd
'''
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出并返回这两个正序数组的 中位数 。
'''

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 处理数组为空的情况
        if not nums1: return self.quick_media(nums2 + nums1)
        if not nums2: return self.quick_media(nums1 + nums2)

        # 处理一个数组完全小于另一个的情况
        if nums1[-1] <= nums2[0]: return self.merged_median(nums1, nums2)
        if nums2[-1] <= nums1[0]: return self.merged_median(nums2, nums1)

        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:  # 奇数
            return self.find_the_small_number(nums1, nums2, (total_len + 1) // 2)
        else:  # 偶数
            left = self.find_the_small_number(nums1, nums2, total_len // 2)
            right = self.find_the_small_number(nums1, nums2, total_len // 2 + 1)
            return (left + right) / 2.0

    # 单个有序数组中位数
    def quick_media(self, arr: [int]):
        length = len(arr)
        return arr[length // 2] if length % 2 == 1 \
            else (arr[length // 2 - 1] + arr[length // 2]) / 2.0

    # 两个有序数组，其中一个完全大于另一个
    def merged_median(self, smaller_nums, bigger_nums):
        smaller_len, bigger_len = len(smaller_nums), len(bigger_nums)
        total_len = smaller_len + bigger_len
        if total_len % 2 == 1:  # 奇数
            mid = (total_len + 1) // 2
            if mid <= smaller_len:
                return smaller_nums[mid - 1]
            else:
                return bigger_nums[mid - smaller_len - 1]
        else:  # 偶数
            mid1 = total_len // 2
            mid2 = mid1 + 1
            val1 = smaller_nums[mid1 - 1] if mid1 <= smaller_len else bigger_nums[mid1 - smaller_len - 1]
            val2 = smaller_nums[mid2 - 1] if mid2 <= smaller_len else bigger_nums[mid2 - smaller_len - 1]
            return (val1 + val2) / 2.0

    # target - 第k小元素，target 是剩余需要找的元素数量
    def find_the_small_number(self, nums1: [int], nums2: [int], target: int):
        index1 = index2 = 0
        len1, len2 = len(nums1), len(nums2)
        while True:
            # 到达边界
            # 若 nums1 已遍历完，则第 k 小的元素必在 nums2 中
            if index1 >= len1: return nums2[index2 + target - 1]
            # 若 nums2 已遍历完，则第 k 小的元素必在 nums1 中
            if index2 >= len2: return nums1[index1 + target - 1]
            # 若 k == 1，只需比较当前 nums1[index1] 和 nums2[index2] 的最小值
            if target == 1: return min(nums1[index1], nums2[index2])
            # 取中进行排除
            mid = target // 2  # 本次循环准备排除mid这么多个数字
            target1 = min(mid, len1 - index1)  # 如果排除nums1的数字，那么将会排除多少个（防止mid大于数组长度）
            target2 = min(mid, len2 - index2)  # 如果排除nums2的数字，那么将会排除多少个（防止mid大于数组长度）
            if nums1[index1 + target1 - 1] <= nums2[index2 + target2 - 1]:
                # nums1 中准备排除的数字更小，进行排除
                index1 += target1
                target -= target1
            else:
                # nums2 中准备排除的数字更小，进行排除
                index2 += target2
                target -= target2

if __name__ == "__main__":
    res = Solution().findMedianSortedArrays([], [1])
    print(res)
