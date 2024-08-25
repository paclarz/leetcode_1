# solved in 14th June 2024

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> [str]:

        res = []
        while len(s) > k:
            res.append(s[:k])
            s = s[k:]

        while len(s) != k:
            s = s + fill

        res.append(s)
        return res
