mapping = {
    "{": "}",
    "}": "{",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
}

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        stack = list()
        for char in s:
            if not stack or stack[-1] != mapping[char]:
                stack.append(char)
            else:
                stack = stack[:-1]
            # print(stack)

        return not stack


def main():
    solution = Solution()
    assert solution.isValid("()")
    assert solution.isValid("()[]{}")
    assert not solution.isValid("(]")
    assert not solution.isValid("([)]")

if __name__ == '__main__':
    main()
