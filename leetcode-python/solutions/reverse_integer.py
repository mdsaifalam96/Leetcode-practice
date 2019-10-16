class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = 2**31
        min_int = -1 * (2**31 - 1)

        multiplier = -1 if x < 0 else 1
        x *= multiplier

        reversed_number = 0
        while x > 0:
            new_digit = x % 10
            reversed_number = (reversed_number * 10) + new_digit
            x //= 10

        reversed_number *= multiplier
        
        # print("reversed_number {}".format(reversed_number))
        return 0 if reversed_number > max_int or reversed_number < min_int \
                else reversed_number
        
def main():
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(2147483648) == 0

if __name__ == '__main__':
    main()
