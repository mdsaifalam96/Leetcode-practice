class Solution:

    def __init__(self):
        self.checked_combos = set()

    def combinationSumHelper(self, candidates, multiples, current_sum, target):
        combos = list()

        for i in range(len(candidates)):
            tmp_multiples = multiples.copy()
            tmp_multiples[i] += 1
            tmp_sum = current_sum + candidates[i]
            combo_key = "-".join([str(x) for x in tmp_multiples])
            if combo_key in self.checked_combos:
                continue
            else:
                self.checked_combos.add(combo_key)
            if tmp_sum == target:
                combo = list()
                for x, y in zip(candidates, tmp_multiples):
                    for i in range(y):
                        combo.append(x)
                combos.append(combo)
            elif tmp_sum < target:
                combos.extend(self.combinationSumHelper(
                    candidates, tmp_multiples, tmp_sum, target))

        return combos

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.combinationSumHelper(candidates, [0] * len(candidates), 0, target)


def main():
    solution = Solution()
    assert solution.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert solution.combinationSum([2, 3, 5], 8) == [
        [2, 2, 2, 2], [2, 3, 3], [3, 5]]


if __name__ == '__main__':
    main()
