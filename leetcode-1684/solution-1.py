from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            flag = True
            for letter in word:
                if letter not in allowed:
                    flag = False

            if flag is True:
                count += 1

        return count
