from solve import Jun_16_2138 as p2138

solve = p2138.Solution().divideString

def ans(self, s: str, k: int, fill: str) -> [str]:
    ans = []

    while s:  # while s is not empty
        ans += s[:k],  # add first k characters to ans
        s = s[k:]  # remove first k characters from s

    ans[-1] += fill * (k - len(ans[-1]))  # add fill characters to last string in ans to make it k characters long
    return ans

def check():
    res1 = solve("abcdefghij", 3, 'x')
    assert res1 == ['abc', 'def', 'ghi', 'jxx'], "incorrect with input ('abcdefghij', 3, 'x')"

    print("check passed")
