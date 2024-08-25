class Solution:
    def maxProfit(self, prices: [int]) -> int:
        orderedList = [[prices[0], prices[0]]]

        for index, value in enumerate(prices):  # 决定这个value的处理办法

            if index == 0:  # 处理第一个value的情况
                continue

            if orderedList[-1][0] > value:  # 如果这个value下跌了
                if orderedList[-1][0] == orderedList[-1][1]:
                    orderedList[-1] = [value, value]  # 更新这一行的最后一个值
                else:
                    orderedList.append([value, value])  # 就新建一行
                continue

            #         如果这个value上涨了

            for jdex, line in enumerate(orderedList):  # 对于已有的二维数组的每一行

                if line[-1] < value:  # 如果这个value上涨了
                    line[-1] = value  # 就追加到这一行末尾

        ans = 0
        for line in orderedList:
            if line[-1] - line[0] > ans:
                ans = line[-1] - line[0]

        return ans
