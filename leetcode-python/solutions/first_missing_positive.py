from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos_set = set([x for x in nums if x > 0])
        i, smallest_pos = 1, None
        while not smallest_pos:
            if i not in pos_set:
                smallest_pos = i
            i += 1

        return smallest_pos
