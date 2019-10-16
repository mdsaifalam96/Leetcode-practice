''' Multiply Strings '''

class Solution:
    ''' Solution class '''

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        place_buckets = dict()

        if (len(num1) == 1 and int(num1) == 0) or (len(num2) == 1 and int(num2) == 0):
            return "0"

        if len(num1) == 1 and int(num1) == 1:
            return num2
        elif len(num2) == 1 and int(num2) == 1:
            return num1

        for index_1, digit_1 in enumerate(num1[::-1]):
            for index_2, digit_2 in enumerate(num2[::-1]):

                # print("multiplying place", str(index_1), "of", num1, \
                #         "with place", str(index_2), "of", num2)

                place = index_1 + index_2
                mul = int(digit_1) * int(digit_2)
                # print("solution is", mul)

                units = mul % 10
                carry_over = mul // 10

                value_to_increment = 0
                if place in place_buckets:
                    value_to_increment = place_buckets[place]
                value_to_increment += units
                place_buckets[place] = value_to_increment % 10
                carry_over += value_to_increment // 10

                while carry_over:
                    place += 1
                    value_to_increment = 0
                    if place in place_buckets:
                        value_to_increment = place_buckets[place]
                    value_to_increment += carry_over
                    place_buckets[place] = value_to_increment % 10
                    carry_over = value_to_increment // 10

        # print(place_buckets)

        final_value = ""
        for index in range(max(place_buckets.keys()), -1, -1):
            final_value += str(place_buckets[index])

        return final_value


def main():
    ''' Main function '''
    solution = Solution()
    print(solution.multiply("13", "20"))
    print(solution.multiply("101", "5"))
    print(solution.multiply("100", "0"))
    print(solution.multiply("753757584327576358248910913018487583465375238" + \
                            "402019840932857365397537503850934987332508930" + \
                            "4850358029850257236",
                            "873467439865847403294374628472384725633758453" + \
                            "265284294382567356247284249284653757395375345" + \
                            "7385023242285798672"))

if __name__ == '__main__':
    main()
