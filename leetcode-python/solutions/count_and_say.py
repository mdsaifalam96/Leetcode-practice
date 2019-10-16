class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return

        current_string = "1"

        if n == 1:
            return current_string

        for _ in range(n - 1):
            sequence_count = 0
            new_string = ""
            prev_char = ""
            for index, char in enumerate(current_string):
                if index == 0 or char == prev_char:
                    sequence_count += 1
                else:
                    new_string += "{}{}".format(sequence_count, prev_char)
                    sequence_count = 1
                prev_char = char

            new_string += "{}{}".format(sequence_count, prev_char)
            current_string = new_string

        return current_string


def main():
    solution = Solution()
    assert solution.countAndSay(1) == "1"
    assert solution.countAndSay(4) == "1211"
    assert solution.countAndSay(5) == "111221"


if __name__ == '__main__':
    main()
