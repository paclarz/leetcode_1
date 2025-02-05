from typing import List

class Paclarz:
    nums1: [int]
    nums2: [int]

    step1: int
    step2: int

    index1: int
    index2: int

    len1: int
    len2: int
    len: int

    def __init__(self, nums1: [int], nums2: [int]):
        self.nums1 = nums1
        self.nums2 = nums2

        self.len1 = len(nums1)
        self.len2 = len(nums2)
        self.len = len(nums1) + len(nums2)

        self.step1 = self.len1 // 2
        self.step2 = self.len2 // 2

        self.index1 = self.len1 // 4
        self.index2 = self.len2 // 4

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


    def get_direction(self):
        if self.index1 + self.index2  -4 < self.len // 2 : return -1
        if self.index1 + self.index2  +8 > self.len // 2 : return 1
        return 0




    def get_state(self) -> [int,int]:
        # nums2 big
        if self.nums1[self.index1] < self.nums2[self.index2 -1] : return  2
        # nums1 big
        if self.nums2[self.index1] < self.nums1[self.index1 -1] : return  1
        return 0

    def go_forward(self):
        direction =  self.get_direction()
        state = self.get_state()
        if direction == 0 and state == 0 :  return 0


        if direction == 1:
            # has too many numbers
            if state == 1 :
        #         nums1 is too big
                return self.forward(True,True)
            elif state == 2 :






        pass

    def forward(self, isNums1: bool, isFoward: bool) -> bool:
        if isNums1:
            if isFoward:
                if self.len1 - 3 == self.index1: return False
                self.index1 += self.step1
            else:
                if self.index1 == 0: return False
                self.index1 -= self.step1
            self.step1 = self.step1 // 2
            if self.step1 <= 0: self.step1 = 1
            if self.index1 < 0: self.index1 = 1
            if self.index1 >= self.len1 - 3: self.index1 = self.len1 - 3
            return True

        else:
            if isFoward:
                if self.len2 - 3 == self.index2: return False
                self.index2 += self.step2
            else:
                if self.index2 == 0: return False
                self.index2 -= self.step2
            self.step2 = self.step2 // 2
            if self.step2 <= 0: self.step2 = 1
            if self.index2 < 0: self.index2 = 1
            if self.index2 >= self.len2 - 3: self.index2 = self.len2 - 3
            return True

    def get_res(self):
        nums1 = []
        if self.len1 - self.nums1.__len__() > 3:
            nums1 = self.nums1[self.index1:self.index1 + 3]
        else:
            nums1 = self.nums1[-3::]
        nums2 = []
        if self.len2 - self.nums2.__len__() > 3:
            nums2 = self.nums2[self.index2:self.index2 + 3]
        else:
            nums2 = self.nums2[-3::]

        res = nums1 + nums2
        res.sort()

        already = self.index1 + self.index2 + 2
        if self.len % 2 == 1:
            return res[self.len // 2 - already + 1]
        else:
            return res[self.len // 2 - already + 1] + res[self.len // 2 - already + 1]



    def is_toomuch(self):
        return self.index1 + self.index2 + 2 > self.len // 2

    def exec(self):
        composed = self.can_be_composed()
        composed.sort()
        if composed:
            if (self.len1 + self.len2) % 2 == 1:
                return composed[composed.__len__() // 2]
            else:
                return (composed[composed.__len__() // 2] + composed[composed.__len__() // 2 + 1]) / 2

        for _ in range(99):
            if self.nums1[self.index1] < self.nums2[self.index2 - 1]:
                # nums2 is too big
                if self.index1 + self.index2 + 2 >= self.len // 2 - 6:
                    # too much
                    self.forward(False,False)
                    continue
                else:
                    self.forward(True, True)
                    continue

            if self.nums1[self.index1]  self.nums2[self.index2 - 1]:
                # nums2 is too big
                if self.index1 + self.index2 + 2 >= self.len // 2 - 6:
                    # too much
                    self.forward(False,False)
                else:
                    self.forward(True, True)

            return self.get_res()

class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return Paclarz(nums1, nums2).exec()

if __name__ == "__main__":
    res = Solution().findMedianSortedArrays([1, 2, 3, 5], [4, 6, 7, 8])
    print(res)
