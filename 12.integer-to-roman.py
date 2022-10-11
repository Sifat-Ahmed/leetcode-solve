class Solution:
    def intToRoman(self, num: int) -> str:
        map = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L',
               40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        result = ''

        ## just keep dividing the number with the roman digits

        for i in reversed(sorted(map.keys())):
            ## checking if divisible
            if num // i:
                ## for seven, i need two I's. So just counting the repeating characters
                count = num // i
                result += (map[i] * count)
                num = num % i
        return result

if __name__ == '__main__':
    s = Solution()
    case = [100, 1, 6, 7, 1, 1235]
    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.intToRoman(case[i])))