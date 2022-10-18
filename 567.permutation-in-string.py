class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## when I am starting this I am not sure how to do
        ## sliding window with hashmap maybe?

        ## s2 should be bigger than s1
        if len(s1) > len(s2): return False

        def create_hashmap(string):
            hashmap = dict()

            for char in string:
                ## if its already there then increment
                if char in hashmap.keys():
                    hashmap[char] += 1
                else:
                    ## else create a new key and update 1
                    hashmap[char] = 1

            return hashmap

        ## creating a dictionary with the first string
        hashmap = create_hashmap(s1)

        ## creating pointers for the window
        left, right = 0, len(s1)

        ## now sliding the window
        while right < len(s2) + 1:

            ## create hashmap for the window
            ## compare the hashmaps
            if hashmap == create_hashmap(s2[left:right]):
                return True

            ## slide one step
            right += 1
            left += 1

        return False
