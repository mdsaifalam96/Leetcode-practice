tens = ["I", "X", "C", "M"]
fives = ["V", "L", "D"]

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        roman_digits = list()
        place = 0
        while num != 0:
            digit = int(num % 10)
            num //= 10
            string = None
            if digit == 9:
                string = tens[place] + tens[place + 1]
            elif digit > 5:
                string = fives[place] + tens[place] * (digit - 5)
            elif digit == 5:
                string = fives[place]
            elif digit == 4:
                string = tens[place] + fives[place]
            elif digit < 4:
                string = tens[place] * digit
            
            roman_digits.append(string)
            place += 1
        
        print("roman_digits: {}".format(roman_digits))

        return "".join(roman_digits[::-1])


def main():
    solution = Solution()
    assert solution.intToRoman(1) == "I"
    assert solution.intToRoman(3949) == "MMMCMXLIX"
    assert solution.intToRoman(3999) == "MMMCMXCIX"
    assert solution.intToRoman(9) == "IX"
    assert solution.intToRoman(520) == "DXX"
    assert solution.intToRoman(535) == "DXXXV"
    assert solution.intToRoman(19) == "XIX"
    assert solution.intToRoman(11) == "XI"
    assert solution.intToRoman(40) == "XL"


if __name__ == '__main__':
    main()
