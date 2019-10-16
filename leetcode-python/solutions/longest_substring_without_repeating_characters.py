''' Longest Substring Without Repeating Characters  '''

class Solution:

    def lengthOfLongestSubstring(self, s):
        max_substring_length = 0
        character_map = dict()

        for index, character in enumerate(s):
            if character in character_map:
                old_index = character_map[character]
                if len(character_map) > max_substring_length:
                    max_substring_length = len(character_map)
                character_map = {k: v for k, v in character_map.items() if v > old_index}
            character_map[character] = index
            # print(character_map)

        if len(character_map) > max_substring_length:
            max_substring_length = len(character_map)

        return max_substring_length

def main():
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring("hdgikkinyyzxycsekxoev"))
    print(solution.lengthOfLongestSubstring("aab"))

if __name__ == '__main__':
    main()
