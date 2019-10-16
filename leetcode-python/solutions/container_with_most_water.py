class Solution:

    def get_area(self, height, front, back):
        return min(height[front], height[back]) * (back - front)

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        front = 0
        back = len(height) - 1
        max_area = self.get_area(height, front, back)
        while front < back:
            # print("front: {}; back: {}".format(front, back))
            area = self.get_area(height, front, back)
            # print("area: {}".format(area))
            max_area = area if area > max_area else max_area

            if height[front] < height[back]:
                front += 1
            else:
                back -= 1

        return max_area


def main():
    solution = Solution()
    assert solution.maxArea([0, 0]) == 0
    assert solution.maxArea([9, 0]) == 0
    assert solution.maxArea([1, 1]) == 1
    assert solution.maxArea([1, 2]) == 1
    assert solution.maxArea([2, 2]) == 2
    assert solution.maxArea([1, 3, 2]) == 2
    assert solution.maxArea([1, 8, 4, 10]) == 16
    assert solution.maxArea([1, 8, 4, 20, 10]) == 24
    assert solution.maxArea([1, 3, 2, 5, 25, 24, 5]) == 24

if __name__ == '__main__':
    main()
