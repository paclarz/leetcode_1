# problem No.1832
# created by setup.py at 2024-06-18 23:01:10
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashList = [0 for _ in range(26)]

        for char in sentence:
            # ord(a) = 97
            hashList[ord(char) - 97] += 1

        for _, value in enumerate(hashList):
            if value == 0:
                return False

        return True
