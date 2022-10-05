class Solution(object):

    def letterCombinations(self, digits):
        map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        if digits == "": return []

        ret = ['']
        for c in digits:
            tmp = []
            for y in ret:
                for x in map[c]:
                    tmp.append(y + x)
            ret = tmp
        return ret


if __name__ == '__main__':
    s = Solution()
    case = ['23', '456', '892']

    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i+1, case[i], s.letterCombinations(case[i])))