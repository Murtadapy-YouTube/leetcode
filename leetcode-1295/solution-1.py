from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for x in nums:
            if len(str(x)) % 2 == 0:
                count += 1

        return count


if __name__ == "__main__":
    s = Solution()

    print(s.findNumbers([18, 2, 1, 10, 20]))
    print(s.findNumbers([20, 3010, 4020, 1]))
