# problem No.1832
# created by setup.py at 2024-06-18 23:01:10

from solve import Jun_18_1832 as Solution

class check:
    def check(self):
        s = Solution.Solution().checkIfPangram

        assert s("thequickbrownfoxjumpsoverthelazydog") == True
