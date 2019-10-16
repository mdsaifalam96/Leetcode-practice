class Solution:

    longest_palindrome_size = -1
    longest_palindrome = None

    def replace_if_longest_palidrome(self, candidate):
        if len(candidate) > Solution.longest_palindrome_size:
            Solution.longest_palindrome = candidate
            Solution.longest_palindrome_size = len(candidate)

    def check_palindrome(self, index_1, index_2, string):
        if index_1 >= 0 and index_2 < len(string) and string[index_1] == string[index_2]:
            return self.check_palindrome(index_1 - 1, index_2 + 1, string)
        else:
            return string[index_1 + 1 : index_2]


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return 0

        Solution.longest_palindrome_size = -1

        for index, _ in enumerate(s):
            palindrome = self.check_palindrome(index - 1, index + 1, s)
            self.replace_if_longest_palidrome(palindrome)

            if index + 1 < len(s) and s[index] == s[index + 1]:
                palindrome = self.check_palindrome(index - 1, index + 2, s)
                self.replace_if_longest_palidrome(palindrome)

        return Solution.longest_palindrome


def main():
    solution = Solution()
    print(solution.longestPalindrome("aabba"))
    print(solution.longestPalindrome("cbbd"))

if __name__ == '__main__':
    main()
