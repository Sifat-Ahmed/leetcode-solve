class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## I will just try this with hashmap, create a hashmap with magazine and then check char by char from ransomNote

        if len(s) != len(t): return False

        hash_table = dict()

        ## firs creating the table with magazine characters
        for i in s:
            if i in hash_table.keys():
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        ## now check with ransomNote str char by char
        ## first the character has to be in hashmap
        ## and need to track the count of that object

        for i in t:
            ## if the char is not in hash, then str can't be produced
            if i not in hash_table.keys():
                return False
            ## if the hash, then check if we can use it because it can be only used once
            elif i in hash_table.keys():
                ## not enough characters
                if hash_table[i] == 0:
                    return False
                ## everything's okay, just update the table
                else:
                    hash_table[i] -= 1

        ## ransomNote can be constructed if code reaches this far
        return True