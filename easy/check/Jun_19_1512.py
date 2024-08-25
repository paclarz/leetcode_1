# problem No.1512
# created by setup.py at 2024-06-19 00:10:15

from solve import Jun_19_1512 as Solution

class check:
    def check(self):
        s = Solution.Solution().numIdenticalPairs

        assert s([1, 2, 3, 1, 1, 3]) == 4
