# problem No.0076
# created by setup.py at 2024-06-17 11:27:06

from solve import Jun_17_0076 as Solution

class check(Solution.Solution):
    def check(self):
        # assert self.minWindow("ADOBECODEBANC", "ABC") == "BANC"
        # assert self.minWindow("a", "a") == "a"
        assert self.minWindow("bdab", "ab") == "ab"
        # assert self.minWindow("aa", "aa") == "aa"

import copy

# 失败解，运行通过，性能问题
class Solution:
    left, right = 0, 0

    TARGET = ""
    STRING = ""

    left_t = ''

    ans_left = -1
    ans_right = -1

    def minWindow(self, s: str, t: str) -> str:
        self.TARGET = copy.deepcopy(t)
        self.STRING = copy.deepcopy(s)

        self.left_t = copy.deepcopy(t)

        # 修改成while循环
        index = -1
        while index < len(s) - 1:
            index += 1
            value = s[index]
            if value in self.left_t:

                self.left_t = self.left_t.replace(value, '', 1)

                if self.left_t == '':
                    self.right = index
                    self.headBack()
                    self.left += 1
                    index = self.left
                    self.right = self.left
                    self.left_t = copy.deepcopy(t)

        print(self.STRING[self.ans_left:self.ans_right + 1])
        if self.ans_right == -1:
            return ""
        return self.STRING[self.ans_left:self.ans_right + 1]

    def headBack(self):
        self.left_t = copy.deepcopy(self.TARGET)

        for index in range(self.right, self.left - 1, -1):
            if self.STRING[index] in self.left_t:
                self.left_t = self.left_t.replace(self.STRING[index], '', 1)
                if self.left_t == '':
                    self.left = index
                    break

        if self.right - self.left < self.ans_right - self.ans_left or self.ans_right == -1:
            self.ans_left = self.left
            self.ans_right = self.right

        pass
