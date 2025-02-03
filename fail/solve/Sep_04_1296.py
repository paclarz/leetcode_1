# problem No.1296
# created by setup.py at 2024-09-04 19:25:48
from typing import List


class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        class counter():

            data = []

            def __getitem__(self, value):
                for [item, count] in self.data:
                    if (item == value):
                        return count
                return 0

            def __setitem__(self, key, value):
                if value < 0:
                    return False
                if value == 0:
                    self.__sub__(key)
                    return True
                for pointer in range(0, self.data.__len__()):
                    if self.data[pointer][0] == key:
                        self.data[pointer][1] = value
                        return True
                self.data.append([key, value])
                return True

            def sort(self):
                def sorter(item):
                    return item[0]

                self.data = sorted(self.data, key=sorter)
                return self.data[0]

            def __str__(self):
                return self.data.__str__()

            def __sub__(self, other: int):
                for index in range(0, len(self.data) - 1):
                    if self.data[index][0] == other:
                        self.data.pop(index)
                        return
                if self.data.__len__() == 1:
                    if (other == self.data[0][0]):
                        self.data.pop(0)

        if nums.__len__() % k != 0:
            return False

        count = counter()
        for item in nums:
            count[item] += 1

        count.sort()

        print(count)

        while len(count.data) > 0:
            head_value, head_count = count.data[0]
            for step in range(0, k):
                if count[head_value + step] < head_count:
                    return False
                count[head_value + step] = count[head_value + step] - head_count

        return True
