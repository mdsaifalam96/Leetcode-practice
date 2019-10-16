class Solution(object):
    def isMatch(self, text, pattern):
        # if no pattern and no text, return True
        if not pattern:
            return not text

        # first character will not be a Kleene star
        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or  # if none of pattern[0] is utilized 
                    first_match and self.isMatch(text[1:], pattern)) # if one of pattern[0] is utilized 
        else:
            return first_match and self.isMatch(text[1:], pattern[1:]) # if one character is consumed


def main():
    solution = Solution()
    assert solution.isMatch("aa","a") == False
    assert solution.isMatch("aa","aa") == True
    assert solution.isMatch("aaa","aa") == False
    assert solution.isMatch("aa", "a*") == True
    assert solution.isMatch("aa", ".*") == True
    assert solution.isMatch("ab", ".*") == True
    assert solution.isMatch("aab", "c*a*b") == True
    assert solution.isMatch("aabc", "c*a*b") == False
    assert solution.isMatch("aabdcc", "a.*c") == True
    assert solution.isMatch("a", ".*..a*") == False
    assert solution.isMatch("ab", ".*..") == True
    assert solution.isMatch("aaa", "a*a") == True
    assert solution.isMatch("aa", "a*") == True
    assert solution.isMatch("a", "ab*") == True

if __name__ == '__main__':
    main()
