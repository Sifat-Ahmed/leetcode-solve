class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ## I will just try this with hashmap, create a hashmap with magazine and then check char by char from ransomNote

        hash_table = dict()

        ## firs creating the table with magazine characters
        for i in magazine:
            if i in hash_table.keys():
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        ## now check with ransomNote str char by char
        ## first the character has to be in hashmap
        ## and need to track the count of that object

        for i in ransomNote:
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


### Solved directly on OJ