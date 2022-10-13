class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

if __name__ == '__main__':
    s = Solution()
    haystack = ['leetcode', 'aaapyy', "sadbutsad", "mississippi"]
    needle = ['tco', 'haaapy', 'sad', "issipi"]

    for i in range(len(haystack)):
        print('Test case {}: {} -> {}'.format(i+1, haystack[i], s.strStr(haystack[i], needle[i])))
