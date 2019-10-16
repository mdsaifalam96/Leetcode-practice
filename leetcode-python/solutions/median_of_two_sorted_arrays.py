class Solution:

    def findMedianOfSortedArray(self, array):
        if len(array) % 2 == 0:
            return (array[(len(array) // 2) - 1] + array[(len(array) // 2)]) / 2
        else:
            return array[(len(array) // 2)]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if not nums1:
            return self.findMedianOfSortedArray(nums2)
        if not nums2:
            return self.findMedianOfSortedArray(nums1)

        (long_list, short_list) = (nums1, nums2) if len(nums1) > len(nums2) else (nums2, nums1)
        # print("short_list: {}, long_list: {}".format(short_list, long_list))

        short_list_min_index, short_list_max_index = 0, len(short_list)
        # print("short_list_min_index: {}; short_list_max_index: {}".format(short_list_min_index, short_list_max_index))

        total_length = len(long_list) + len(short_list)
        # print("total_length: {}".format(total_length)) 

        while short_list_min_index <= short_list_max_index:
            short_list_index = (short_list_min_index + short_list_max_index) // 2
            long_list_index = ((total_length + 1) // 2) - short_list_index
            # print("short_list_index: {}; long_list_index: {}".format(short_list_index, long_list_index))

            if short_list_index < len(short_list) and long_list[long_list_index - 1] > short_list[short_list_index]:
                short_list_min_index = short_list_index + 1
            elif short_list_index > 0 and short_list[short_list_index - 1] > long_list[long_list_index]:
                short_list_max_index = short_list_index - 1
            else:
                if short_list_index == 0:
                    max_left = long_list[long_list_index - 1]
                elif long_list_index == 0:
                    max_left = short_list[short_list_index - 1]
                else:
                    max_left = max(short_list[short_list_index - 1], long_list[long_list_index - 1])
                # print("max_left: {}".format(max_left))
                
                if total_length % 2 != 0:
                    return max_left
                
                if short_list_index == len(short_list):
                    min_right = long_list[long_list_index]
                elif long_list_index == len(long_list):
                    min_right = short_list[short_list_index]
                else:
                    min_right = min(short_list[short_list_index], long_list[long_list_index])
                # print("min_right: {}".format(min_right))

                return (max_left + min_right) / 2


def main():
    solution = Solution()
    assert solution.findMedianSortedArrays([1, 2, 4], []) == 2
    assert solution.findMedianSortedArrays([1, 2, 4], [3]) == 2.5
    assert solution.findMedianSortedArrays([1, 2], [2, 3, 4]) == 2
    assert solution.findMedianSortedArrays([1, 2, 4], [2, 3]) == 2
    assert solution.findMedianSortedArrays([1, 2, 4], [2, 3, 6]) == 2.5
    assert solution.findMedianSortedArrays([1, 2, 4], [6, 7]) == 4
    assert solution.findMedianSortedArrays([1, 3], [2]) == 2
    assert solution.findMedianSortedArrays([1], [1]) == 1

if __name__ == '__main__':
    main()
