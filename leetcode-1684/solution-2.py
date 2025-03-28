from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    break
            else:
                count += 1
        return count
