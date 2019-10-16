class Solution:
    
    def check_common_character(self, index, strs):
        if index >= len(strs[0]):
            return False
        char = strs[0][index]

        for string in strs[1:]:
            if index >= len(string) or string[index] != char:
                return False

        return True


    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]

        index = 0
        while self.check_common_character(index, strs):
            index += 1

        return strs[0][:index]


def main():
    solution = Solution()
    str_0 = ""
    str_1 = "abcd"
    str_2 = "abc"
    str_3 = "abd"
    str_4 = "xyz"

    assert solution.longestCommonPrefix([]) == ""
    assert solution.longestCommonPrefix([str_1, str_2]) == "abc"
    assert solution.longestCommonPrefix([str_1, str_2, str_3]) == "ab"
    assert solution.longestCommonPrefix([str_0, str_2, str_3]) == ""
    assert solution.longestCommonPrefix([str_1, str_2, str_4]) == ""

if __name__ == '__main__':
    main()
