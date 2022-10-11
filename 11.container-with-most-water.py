class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height)-1
        area = 0

        while left < right:
            temp_area = (min(height[left], height[right]) * (right - left))

            if area < temp_area : area = temp_area

            if height[right] < height[left] : right -= 1
            else : left += 1

        return area

if __name__ == '__main__':
    s = Solution()
    case = [[1,8,6,2,5,4,8,3,7], [1,1]]
    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.maxArea(case[i])))
