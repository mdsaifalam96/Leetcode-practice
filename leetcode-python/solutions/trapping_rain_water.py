from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        n = len(height)
        max_l, max_r = [height[0]], [height[n-1]]
        for i in range(1, n):
            li, ri = i, n - i - 1
            max_l.append(max(height[li], max_l[-1]))
            max_r.append(max(height[ri], max_r[-1]))
        max_r.reverse()

        wc = 0
        for i in range(n):
            wc += min(max_l[i], max_r[i]) - height[i]

        return wc
