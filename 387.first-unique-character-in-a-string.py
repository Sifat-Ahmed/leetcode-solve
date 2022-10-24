class Solution:
    def firstUniqChar(self, s: str) -> int:
        ## create a hashmap and then check if the element has a count value greater than 1

        ## Solved directly on the ide

        hashmap = dict()

        for i in s:
            if i in hashmap.keys():
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        count = 0
        for i in s:
            if not hashmap[i] > 1:
                return count

            count += 1

        if count == len(s): return -1