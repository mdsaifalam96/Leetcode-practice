class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        stack = list()
        max_diff = 0

        for index, char in enumerate(s):

            # print("index: {}; stack: {}".format(index, stack))
            if not stack or char == '(':
                stack.append((char, index))
            elif stack[-1][0] == '(':
                stack.pop()
                diff = index - stack[-1][1] if stack else index + 1
                max_diff = diff if diff > max_diff else max_diff
                # print("max_diff: {}".format(max_diff))
            else:
                stack.append((char, index))

        return max_diff


def main():
    solution = Solution()
    assert solution.longestValidParentheses("") == 0
    assert solution.longestValidParentheses("()") == 2
    assert solution.longestValidParentheses("()(") == 2
    assert solution.longestValidParentheses("(()") == 2
    assert solution.longestValidParentheses(")()())") == 4
    assert solution.longestValidParentheses(")(()())") == 6
    assert solution.longestValidParentheses(")(())())") == 6
    assert solution.longestValidParentheses(")(())((") == 4
    assert solution.longestValidParentheses(")()())()()(") == 4


if __name__ == '__main__':
    main()
