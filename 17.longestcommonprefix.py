"""
problem: https://leetcode.com/problems/longest-common-prefix/description/
Date: 03/10/2022

"""
class Solution(object):
    def word2word(self, word1, word2):
        ## creating a variable to save the substring
        subs = ''
        ## loop variable
        i, j = 0, 0
        ## getting the length of the minimum string
        min_l = min(len(word1), len(word2))
        ## loop through the words
        for i in range(min_l):
            if word1[i] != word2[i]:
                break
            else:
                subs += word1[i]
        return subs

    def common_prefix(self, array, low, high):
        if low == high:
            return array[low]
        if high > low:
            mid = low + (high - low) // 2
            pref1 = self.common_prefix(array, low, mid)
            pref2 = self.common_prefix(array, mid + 1, high)

            return self.word2word(pref1, pref2)

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        ## Will try divide and conquere, Given a list of words, it will be divided into two and the operation
        ## will keep going

        return self.common_prefix(strs, 0, len(strs)-1)

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['hello', 'hell', 'helllaa']))