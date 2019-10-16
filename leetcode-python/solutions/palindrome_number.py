divisor = 10

class Solution:

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        print("checking: {}".format(x))

        if 0 <= x and x < divisor:
            return True
        elif x < 0:
            return False

        num_digits = 1
        while x // (divisor ** num_digits) != 0:
            num_digits += 1

        print("num_digits: ", num_digits)
        new_x = 0
        for i in range(num_digits // 2):
            new_x += (x % divisor) * (divisor ** (num_digits // 2 - (i + 1)))
            x //= divisor
        
        if num_digits % 2 == 1:
            x //= divisor
        
        print("x", x)
        print("new_x", new_x)
        return x == new_x

def main():
    solution = Solution()
    print(solution.isPalindrome(1))
    print(solution.isPalindrome(12))
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(1000021))
    print(solution.isPalindrome(47483648))
    print(solution.isPalindrome(47488474))
    print(solution.isPalindrome(4748474))
    print(solution.isPalindrome(-2147483648))
    print(solution.isPalindrome(2147483647))

if __name__ == '__main__':
    main()
