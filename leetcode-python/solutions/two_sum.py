''' Two Sum '''

class Solution:
    ''' Solution class '''

    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''
        complement_map = dict()
        for index, num in enumerate(nums):
            complement = target - num
            if complement in complement_map:
                return complement_map[complement], index
            else:
                complement_map[num] = index

        return ()


def main():
    ''' Main function '''
    solution = Solution()
    print(solution.twoSum([1, 2, 3, 4], 5))

if __name__ == '__main__':
    main()
