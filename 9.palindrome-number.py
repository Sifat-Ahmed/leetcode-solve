class Solution:
    def isPalindrome(self, x: int) -> bool:
        ## just reverse the number and check if they are equal
        if x < 0: return False
        reverse = 0
        temp = x

        while(temp != 0):
            reverse = (reverse * 10) + (temp % 10)
            temp = temp // 10

        return x == reverse

if __name__ == '__main__':
    s = Solution()
    case = [100, 1, 0, -100, 121, 12365456321]
    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.isPalindrome(case[i])))