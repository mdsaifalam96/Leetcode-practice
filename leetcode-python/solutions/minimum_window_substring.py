''' Minimum Window Substring '''

import collections

class Solution:
    ''' Solution class '''

    def minWindow(self, string, target):

        expected_characters = collections.Counter(target)
        missing_char_count = len(target)
        i = start_index = end_index = 0

        for j, character in enumerate(string, 1):
            missing_char_count -= expected_characters[character] > 0
            expected_characters[character] -= 1

            if not missing_char_count:
                while i < j and expected_characters[string[i]] < 0:
                    expected_characters[string[i]] += 1
                    i += 1
                if not end_index or j - i < end_index - start_index:
                    start_index, end_index = i, j

        return string[start_index:end_index]


def main():
    ''' Main function '''
    solution = Solution()
    # print(solution.minWindow("a", "aa"))
    print(solution.minWindow("ADOBECODEBANC", "ABC"))
    # print(solution.minWindow("ADOBECODEBANC", "ABCD"))
    # print(solution.minWindow("ADOBECODEBANC", "ABCDE"))
    # print(solution.minWindow("ADOBECODEBANC", "ABCDEF"))

if __name__ == '__main__':
    main()
