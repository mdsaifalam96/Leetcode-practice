class Solution:
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """

        if not string:
            return 0

        max_int = (2 ** 31) - 1
        min_int = -1 * (2 ** 31)

        max_string_len = len(str(max_int))

        multiplier = 1
        start_index = None
        for index, char in enumerate(string):
            if char != ' ':
                start_index = index
                break
        # print("start_index: {}".format(start_index))

        if (string[start_index] == '+' or string[start_index] == '-') \
                and index + 1 < len(string) \
                and string[index + 1].isdigit():
            multiplier = -1 if char == '-' else 1
            start_index = index + 1
        
        number_string = ""
        for index in range(start_index, len(string)):
            if string[index].isdigit():
                number_string += string[index]
            else:
                break
        # print("number_string: {}".format(number_string))

        if len(number_string) > max_string_len:
            if multiplier == 1:
                return max_int
            else:
                return min_int

        if number_string:
            number = int(number_string) * multiplier
            # print("number: {}".format(number))

            if number < min_int:
                return min_int
            elif number > max_int:
                return max_int
            else:
                return number

        return 0


def main():
    solution = Solution()
    assert solution.myAtoi("") == 0
    assert solution.myAtoi("   123   ") == 123
    assert solution.myAtoi("   123adkew") == 123
    assert solution.myAtoi("   +123adkew") == 123
    assert solution.myAtoi("   -123adkew") == -123
    assert solution.myAtoi("   -adkew") == 0
    assert solution.myAtoi("   -adkew12312") == 0
    assert solution.myAtoi("      -11919730356x") == -2147483648

if __name__ == '__main__':
    main()
