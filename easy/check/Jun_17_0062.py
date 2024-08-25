# problem No.0062
# created by setup.py at 2024-06-17 11:02:25

from solve import Jun_17_0062 as Solution

class check(Solution.Solution):
    def check(self):
        assert self.uniquePaths(3, 7) == 28
        assert self.uniquePaths(3, 2) == 3
        assert self.uniquePaths(7, 3) == 28
