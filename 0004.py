from typing import List


class Paclarz:
    isNums1 = False
    isForward = False

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.length = self.nums1.__len__() + self.nums2.__len__()
        self.isOdd = (self.length % 2 == 1)

        self.index1 = self.step1 = self.nums1.__len__() // 2
        self.index2 = self.step2 = self.nums2.__len__() // 2

        self.step1 -= 1
        self.step2 -= 1

    def can_be_composed(self):
        if self.nums1.__len__() <= 3 or self.nums2.__len__() <= 3:
            res = self.nums2 + self.nums1
            res.sort()
            return res
        if self.nums1[-1] <= self.nums2[0]:
            return self.nums1 + self.nums2
        if self.nums2[-1] <= self.nums1[0]:
            return self.nums2 + self.nums1

        return []

    def forward(self, isNums1: bool, isFoward: bool):
        if isNums1:
            if isFoward:
                self.index1 += self.step1
            else:
                self.index1 -= self.step1
            self.step1 = self.step1 // 2
            if self.step1 <= 0: self.step1 = 1
            if self.index1 < 0: self.index1 = 1

        else:
            if isFoward:
                self.index2 += self.step2
            else:
                self.index2 -= self.step2
            self.step2 = self.step2 // 2
            if self.step2 <= 0: self.step2 = 1
            if self.index2 < 0: self.index2 = 1

        print("current index : ", self.index1, " -- ", self.index2)

    def get_mid(self):
        if self.isOdd:
            opt1, opt2 = self.nums1[self.index1], self.nums2[self.index2]
            return opt1 if opt1 < opt2 else opt2
        else:
            opts = []
            if self.index1 == self.nums1.__len__() - 1:
                opts += [self.nums1[-1], - float('inf')]
            else:
                opts += self.nums1[self.index1: self.index1 + 2]
            if self.index2 == self.nums2.__len__() - 1:
                opts += [self.nums2[-1], - float('inf')]
            else:
                opts += self.nums2[self.index2: self.index2 + 2]
            opts.sort()
            return (opts[1] + opts[2]) / 2

    def exec(self) -> float:

        composed = self.can_be_composed()
        if composed:
            if composed.__len__() == 1: return composed[0]
            if self.isOdd:
                return composed[self.length // 2]
            else:
                return (composed[self.length // 2] + composed[self.length // 2 - 1]) / 2

        for _ in range(99):

            if self.nums1[self.index1 - 1 if self.index1 != 0 else 0] > self.nums2[self.index2]:
                # nums1 is bigger
                if self.index1 + self.index2 + 2 > self.length / 2:
                    # too much
                    self.forward(True, False)
                    self.isNums1, self.isForward = True, True
                    continue
                else:
                    # not enough
                    self.forward(False, True)
                    self.isNums1, self.isForward = False, True
                    continue

            if self.nums1[self.index1] < self.nums2[self.index2 - 1 if self.index2 != 0 else 0]:
                # nums2 is bigger
                if self.index1 + self.index2 + 2 > self.length / 2:
                    # too much
                    self.forward(False, False)
                    self.isNums1, self.isForward = False, False
                    continue
                else:
                    # not enough
                    self.forward(True, True)
                    self.isNums1, self.isForward = True, True
                    continue

            if self.index1 + self.index2 + 2 == self.length // 2:
                return self.get_mid()

            if self.index1 + self.index2 < self.length // 2 and self.nums1.__len__() < self.index1 + 1 and self.nums1[
                self.index1] == self.nums1[self.index1 + 1]:
                self.index1 += 1
            elif self.index1 + self.index2 < self.length // 2 and self.nums2.__len__() < self.index2 + 1 and self.nums2[
                self.index2] == self.nums2[self.index2 + 1]:
                self.index2 += 1
            elif self.index1 + self.index2 > self.length // 2 and self.index1 > 0 and self.nums1[self.index1] == \
                    self.nums1[self.index1 - 1]:
                self.index1 -= 1
            elif self.index1 + self.index2 > self.length // 2 and self.index2 > 0 and self.nums2[self.index2] == \
                    self.nums2[self.index2 - 1]:
                self.index2 -= 1
            elif self.index1 + self.index2 + 2 > self.length // 2:

                self.forward(not self.isNums1, False)
                self.isNums1, self.isForward = not self.isNums1, False
                # continue
            else:
                self.forward(not self.isNums1, True)
                self.isNums1, self.isForward = not self.isNums1, True
                # continue


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return Paclarz(nums1, nums2).exec()


if __name__ == "__main__":
    res = Solution().findMedianSortedArrays([1, 2, 3, 5], [4, 6, 7, 8])
    print(res)
