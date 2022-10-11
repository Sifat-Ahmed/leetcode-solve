class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if len(s) == 0:
            return 0

        number = 0
        count = 0
        sign = -1 if s[0] == '-' else 1

        for i in s:
            if i.isdigit():
                number = (number * 10) + int(i)
                count = 1
            elif (i == '+' or i == '-') and count == 0:
                count = 1
                continue
            else: break
        number = number * sign

        if -2 ** 31 <= number <= (2 ** 31) - 1:
            return number
        elif number < 0:
            return -2 ** 31
        else:
            return 2 ** 31 - 1

if __name__ == '__main__':
    s = Solution()
    case = ["-123", "+-12", "0032", "89999999999", "words and 42", "-5222 and words", "-6523+"]
    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.myAtoi(case[i])))