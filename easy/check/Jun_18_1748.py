# problem No.1748
# created by setup.py at 2024-06-18 22:25:12

from solve import Jun_18_1748 as Solution

class check:
    def check(self):
        func = Solution.Solution().sumOfUnique

        # assert func([1, 2, 3, 2, 1]) == 5
        # assert func([1, 1, 1, 1, 1]) == 0
        assert func([1, 2, 3, 4, 5]) == 15
