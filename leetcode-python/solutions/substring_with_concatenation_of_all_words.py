''' Substring with Concatenation of All Words '''

class Solution:
    ''' Solution class '''

    def findSubstring(self, string, words):
        '''
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        '''

        if not words or not string:
            return []

        unit_length = len(words[0])
        # print(string, len(string))
        # print(words, len(words), "x", unit_length)

        word_dict = dict()
        word_index = 1
        for word in words:
            if word in word_dict:
                continue
            word_dict[word] = word_index
            word_index += 1
        # print("word_dict:", word_dict)

        desired_marker = 0
        for word in words:
            desired_marker += word_dict[word]
        # print("desired_marker:", desired_marker)

        index = 0
        word_presence_representation = list()
        while index < (len(string) - unit_length) + 1:
            sub_string = string[index : (index + unit_length)]
            if sub_string in word_dict:
                word_presence_representation.append(word_dict[sub_string])
            else:
                word_presence_representation.append(0.1)
            index += 1
        # print(word_presence_representation, len(word_presence_representation))

        combo_presence_representation = list()
        index = 0
        while index < len(string) - (unit_length * len(words)) + 1:
            sum_of_markers = 0
            for sub_index in range(len(words)):
                sum_of_markers += \
                    word_presence_representation[index + (sub_index * unit_length)]
            combo_presence_representation.append(sum_of_markers)
            index += 1
        # print(combo_presence_representation, len(combo_presence_representation))

        locations = [i for i, x in enumerate(combo_presence_representation) if x == desired_marker]
        return locations


def main():
    ''' Main function '''
    solution = Solution()
    print(solution.findSubstring("sheateateseatea", ["sea", "tea", "ate"]))
    print(solution.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", \
                                ["fooo", "barr", "wing", "ding", "wing"]))
    print(solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
    print(solution.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
    print(solution.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(solution.findSubstring("", ["foo", "bar"]))
    print(solution.findSubstring("barfoothefoobarman", ["foo"]))
    print(solution.findSubstring("barfoothefoobarbazman", ["foo", "baz", "bar"]))

if __name__ == '__main__':
    main()
