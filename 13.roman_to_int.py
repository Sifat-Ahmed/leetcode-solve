class Solution(object):
    def __int__(self):
        pass

    def romanToInt(self, s):
        roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        number = 0
        for i in range(len(s)):
            if ((i + 1) < len(s)) and (roman_dict[s[i+1]] > roman_dict[s[i]]):
                number -= roman_dict[s[i]]
            else:
                number += roman_dict[s[i]]

        return number

if __name__ == '__main__':
    s = Solution()
    case = ['III', 'LVIII', 'MCMXCIV']

    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i+1, case[i], s.romanToInt(case[i])))