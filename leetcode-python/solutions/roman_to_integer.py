letters = ["I", "V", "X", "L", "C", "D", "M"]

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        total_value = 0
        roman_numeral_index = 0
        for index in range(len(letters) - 1, -1, -1):
            power = index // 2
            current_letter = letters[index]
            current_letter_count = 0
            # print("index: {}, power: {}, letter: {}".format(index, power, current_letter))

            current_letter_count = 0
            multiplicative_factor = 5 if index % 2 else 1
            while roman_numeral_index < len(s) and current_letter == s[roman_numeral_index]:
                current_letter_count += 1
                roman_numeral_index += 1
            value = current_letter_count * (10 ** power) * multiplicative_factor

            if (roman_numeral_index + 1) < len(s) and s[roman_numeral_index + 1] == current_letter:
                offset = 2 if index % 2 == 0 else 1
                subtracting_number_index = index - offset
                value += (10 ** power) * multiplicative_factor
                value -= (10 ** ((subtracting_number_index) // 2)) * (5 if (subtracting_number_index) % 2 else 1)
                roman_numeral_index += 2
            
            total_value += value

        # print("total_value: {}".format(total_value))
        return total_value


def main():
    solution = Solution()
    assert solution.romanToInt("I") == 1
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("IV") == 4
    assert solution.romanToInt("V") == 5
    assert solution.romanToInt("VI") == 6
    assert solution.romanToInt("XIX") == 19
    assert solution.romanToInt("DXX") == 520
    assert solution.romanToInt("CD") == 400
    assert solution.romanToInt("MMMCMXLIX") == 3949

if __name__ == '__main__':
    main()
