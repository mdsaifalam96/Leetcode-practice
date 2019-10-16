number_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

cache = dict()

class Solution:

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        combos = list()
        digit = digits[0]
        for char in number_map[digit]:
            remaining_chars = digits[1:]
            if remaining_chars in cache:
                remaining_char_candidates = cache[remaining_chars]
            else:
                remaining_char_candidates = self.letterCombinations(remaining_chars)
                cache[remaining_chars] = remaining_char_candidates

            if not remaining_char_candidates:
                combos.append(char)
            else:
                for remaining_char_candidate in remaining_char_candidates:
                    candidate = char + remaining_char_candidate
                    combos.append(candidate)

        return combos


def main():
    solution = Solution()
    assert solution.letterCombinations("") == []
    assert solution.letterCombinations("2") == ['a', 'b', 'c']
    assert solution.letterCombinations("23") == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    
if __name__ == '__main__':
    main()
