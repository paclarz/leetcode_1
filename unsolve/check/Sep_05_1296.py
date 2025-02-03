# problem No.1296
# created by setup.py at 2024-09-05 09:24:40

from solve import Sep_05_1296 as Solution


class check():
    def check(self):
        s = Solution.Solution().isPossibleDivide

        # res = s([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3)
        res = s([1, 1, 2, 2, 3, 3], 2)

        print(res)
