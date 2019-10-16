class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows < 2:
            return s

        final_lists = dict()
        for i in range(numRows):
            final_lists[i] = list()
        
        list_index_to_assign = 0
        cycle_point = (2 * numRows) - 2
        direction = -1
        # print(list_index_to_assign)
        for index, char in enumerate(s):
            
            if index % cycle_point == 0 or index % cycle_point == numRows - 1:
                direction *= -1
            
            assigned_list = final_lists[list_index_to_assign]
            assigned_list.append(char)
            
            list_index_to_assign += direction
            # print(list_index_to_assign)
            
        final_list = list()
        for i in range(numRows):
            final_list.extend(final_lists[i])
            
        return "".join(final_list)


def main():
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3))
    print(solution.convert("PAYPALISHIRING", 4))

if __name__ == '__main__':
    main()

