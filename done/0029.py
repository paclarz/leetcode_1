class Solution:
    def forward(self, begin, dividend, divisor):

        # 到达最接近的位置，不能再+1
        if dividend == begin or begin + divisor > dividend:
            return 0

        count = 2
        while count * divisor + begin < dividend:
            count *= 2
        count /= 2

        return count + self.forward(count * divisor + begin, dividend, divisor)

    def divide(self, dividend: int, divisor: int) -> int:

        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        # if abs(divisor) == 1: return dividend * divisor
        # 考虑被除数为最小值的情况
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX

        if divisor == 0: return 0

        positive = dividend * divisor > 0
        res = int(self.forward(0, abs(dividend), abs(divisor)))
        return res if positive else -res


if __name__ == '__main__':
    s = Solution().divide(22, -22)
    print(s)
