''' Text Justification '''

class Solution:
    ''' Solution class '''

    def fullJustify(self, words, max_width):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        separate_lines = list()
        current_line = list()
        current_line_char_count = 0
        index = 0
        while index < len(words):
            space = 0 if not current_line else 1
            word_len = len(words[index])
            occupied_space = current_line_char_count + word_len + space
            # print(words[index], occupied_space)
            if occupied_space > max_width:
                separate_lines.append((current_line, current_line_char_count))
                current_line = list()
                current_line_char_count = 0
            else:
                current_line.append((words[index], word_len))
                current_line_char_count = occupied_space
                index += 1

        if current_line:
            separate_lines.append((current_line, current_line_char_count))

        # print(separate_lines)

        justified_lines = []
        for line_tuple_index in range(len(separate_lines)):
            total_spaces_to_add = max_width - separate_lines[line_tuple_index][1]
            # print("total_spaces_to_add:", total_spaces_to_add)

            line_words = separate_lines[line_tuple_index][0]
            division_slots = len(line_words) - 1
            actual_line = ""

            if division_slots == 0:
                actual_line += line_words[0][0]
                for _ in range(total_spaces_to_add):
                    actual_line += " "
            elif line_tuple_index == len(separate_lines) - 1:
                division_slot = 0
                for division_slot in range(division_slots):
                    actual_line += line_words[division_slot][0] + " "
                actual_line += line_words[division_slot + 1][0]
                actual_line += total_spaces_to_add * " "
            else:
                spaces_per_word = total_spaces_to_add // division_slots
                # print("spaces_per_word:", spaces_per_word)
                remainder = total_spaces_to_add % division_slots
                # print("remainder:", remainder)
                division_slot = 0
                for division_slot in range(division_slots):
                    actual_line += line_words[division_slot][0]
                    word_space = 1 + spaces_per_word + (1 if division_slot < remainder else 0)
                    actual_line += word_space * " "
                actual_line += line_words[division_slot + 1][0]

            # print(actual_line, len(actual_line))
            justified_lines.append(actual_line)
        return justified_lines

def main():
    ''' Main function '''
    solution = Solution()
    # print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    # print(solution.fullJustify(["a", "b", "c", "d", "e"], 1))
    print(solution.fullJustify(["What", "must", "be", "shall", "be."], 12))

if __name__ == '__main__':
    main()
