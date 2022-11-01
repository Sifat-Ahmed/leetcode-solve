class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ## first thing first, if length is not equal

        if len(s) != len(t): return False

        ## I will just do hashmap. if the characters are unique in the first string
        ## then just check if there is a repeating character

        hashmap = dict()

        for char1, char2 in zip(s, t):
            ## if the character is not in the hashmap, insert both as key-value pair
            if char1 not in hashmap.keys():
                hashmap[char1] = char2
            ## same character must have corresponding same character which is seen before
            elif hashmap[char1] != char2:
                return False

        return True
