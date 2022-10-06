class Solution:
    def longestPalindrome(self, s: str):
        res = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            tmp = s[l + 1:r]
            if len(tmp) > len(res):
                res = tmp

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            tmp = s[l + 1:r]

            if len(tmp) > len(res):
                res = tmp
        return res
if __name__ == '__main__':
    s = Solution()
    case = ['babad', 'cbbd', ' a ', 'b']

    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i+1, case[i], s.longestPalindrome(case[i])))