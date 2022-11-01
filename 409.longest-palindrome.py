class Solution:
    def longestPalindrome(self, s: str) -> int:
        ## i will try this with hashmap
        if len(s) == 1: return 1

        result = 0
        hashmap = dict()

        ## first creating a hashmap to count the values
        for char in s:
            if char not in hashmap.keys():
                hashmap[char] = 1
            else:
                hashmap[char] += 1

        result, odd = 0, 0

        ## now for every char
        for key in hashmap.keys():
            ## if even then just directly add it
            if hashmap[key] % 2 == 0:
                result += hashmap[key]
            else:
                ## if odd then add key/value-1
                result += hashmap[key] - 1
                ## carry an odd
                odd = 1

        return result + odd