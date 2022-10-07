class Solution:
    def reverse(self, x: int) -> int:
        isNeg = True if x < 0 else False

        x = x * (-1) if isNeg else x

        reverse = 0
        temp = x

        while(temp != 0):
            reverse = (reverse * 10) + (temp % 10)
            temp = temp // 10

        reverse = reverse * (-1) if isNeg else reverse

        if not -2 ** 31 <= reverse <= 2 ** 31:
            return 0

        return reverse

if __name__ == '__main__':
    s = Solution()
    case = [1534236469, 1, 0, -100, 121, 12365456321]
    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.reverse(case[i])))