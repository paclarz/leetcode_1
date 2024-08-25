# problem No.0076
# created by setup.py at 2024-06-17 11:27:06

# problem 当右侧指针移动时，左侧指针应当可能移动多次


import copy

class Solution:
    HASH = [0 for _ in range(70)]
    STRING = ""
    res = ""
    currentHash = []

    unFullFilled = 0

    def setHash(self, s: str):
        for _, i in enumerate(s):
            self.HASH[ord(i) - 60] = self.HASH[ord(i) - 60] + 1
        # 小写字母的范围是 97（'a'） 到 122（'z'）
        # 大写字母的范围是 65（'A'） 到 90（'Z'）
        self.currentHash = copy.deepcopy(self.HASH)
        for index, value in enumerate(self.currentHash):
            if value != 0:
                self.unFullFilled += 1

        for index, value in enumerate(self.currentHash):
            if value == 0:
                self.currentHash[index] = float("-inf")

    def addChar(self, s: chr):
        self.currentHash[ord(s) - 60] = self.currentHash[ord(s) - 60] - 1
        if self.currentHash[ord(s) - 60] == 0:
            self.unFullFilled -= 1
        # elif self.currentHash[ord(s) - 60] == 1:
        #     self.unFullFilled += 1

    def removeChar(self, s: chr):
        self.currentHash[ord(s) - 60] = self.currentHash[ord(s) - 60] + 1
        if self.currentHash[ord(s) - 60] == 0:
            self.unFullFilled -= 1
        # elif self.currentHash[ord(s) - 60] == -1:
        #     self.fullFilled += 1

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        self.setHash(t)

        left, right = 0, 0

        for index, value in enumerate(s):
            # about right pointer
            self.addChar(value)
            right += 1

            # about left pointer
            if (self.currentHash[ord(value) - 60] < 0):
                right += 1

            # about result

            if self.unFullFilled == 0 and len(self.res) > right - left:
                self.res = s[left:right + 1]

            pass
