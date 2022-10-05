class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp, length = "", 0
        for i in range(len(s)):
            if s[i] in tmp:
                length = max(len(tmp), length)
                ind = tmp.index(s[i])
                tmp = tmp[ind + 1:]

            tmp += s[i]
        return max(len(tmp), length)


if __name__ == '__main__':
    s = Solution()
    case = ["abac", "bbbbb", "pwwkew", "a  ", "aaabbbaccc" , "dvdf"]
    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.lengthOfLongestSubstring(case[i])))