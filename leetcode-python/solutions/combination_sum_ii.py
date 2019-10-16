class Solution:
    def comboHelper(self, candidates, answers, current, current_sum, target):
        if current_sum == target:
            answers.add("-".join(current))
            return
        
        if not candidates:
            return

        added = candidates[0] + current_sum
        if added <= target:
            self.comboHelper(candidates[1:], answers, current + [str(candidates[0])], added, target)
            self.comboHelper(candidates[1:], answers, current, current_sum, target)
        else:
            self.comboHelper(candidates[1:], answers, current, current_sum, target)


    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answers = set()
        self.comboHelper(sorted(candidates), answers, list(), 0, target)
        
        results = list()
        for answer in sorted(answers):
            results.append([int(x) for x in answer.split("-")])
        
        return results



def main():
    sol = Solution()
    assert sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert sol.combinationSum2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]

if __name__ == '__main__':
    main()
