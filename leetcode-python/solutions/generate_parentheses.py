class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def get_combo(candidates, combination, open_count, close_count):
            if len(combination) == 2 * n:
                candidates.append(combination)
            else:
                if open_count < n:
                    candidates = get_combo(candidates, combination +
                                           "(", open_count + 1, close_count)
                if close_count < open_count:
                    candidates = get_combo(candidates, combination + ")",
                                           open_count, close_count + 1)

            return candidates

        return get_combo([], "", 0, 0)


def main():
    solution = Solution()
    assert solution.generateParenthesis(1) == ['()']
    assert solution.generateParenthesis(2) == ['(())', '()()']
    assert solution.generateParenthesis(
        3) == ['((()))', '(()())', '(())()', '()(())', '()()()']


if __name__ == '__main__':
    main()
