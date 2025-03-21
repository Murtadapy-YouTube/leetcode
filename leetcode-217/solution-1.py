from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x] == nums[y]:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))
    print(s.containsDuplicate([1, 2, 3]))
