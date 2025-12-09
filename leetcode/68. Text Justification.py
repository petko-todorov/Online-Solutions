# https://leetcode.com/problems/text-justification/description/
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        count = 0
        while True:
            for w in words:
                result.append(' ' * maxWidth)
                if len(result[count]) < maxWidth:
                    result.append(w)
                else:
                    count += 1
                    result.append(w)

            print(result)


words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
         "is", "everything", "else", "we", "do"]
maxWidth = 20

s = Solution()

print(s.fullJustify(words, maxWidth))
