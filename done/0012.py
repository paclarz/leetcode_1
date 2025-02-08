class Solution:
    ans = [
        ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        ['', 'M', 'MM', 'MMM']
    ]

    def intToRoman(self, num: int) -> str:
        num = str(num)
        # fill to 4 digits
        num = '0' * (4 - len(num)) + num
        ans = ''

        for index, number in enumerate(num):
            ans += self.ans[3 - index][int(number)]

        return ans


# Test the code
if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(2345))
