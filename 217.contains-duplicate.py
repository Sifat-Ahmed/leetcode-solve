class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        ## I can do it with one line code. Convert the list to set and check their length
        ## return len(set(nums)) != len(nums)

        ## but I am solving ds problems. SO I will just try this with dict

        # map = dict()
        #
        # ## for every num in the list
        # for num in nums:
        #     ## if it is not in the dictionary
        #     if num not in map.keys():
        #         map[num] = 1 # 1 is just a dummy value. As I am not using it, so it doesn't matter
        #     else:
        #         ## means its already there in the dict
        #         return True
        #
        # ## duplicate not found, return false
        # return False

        ## The above one takes longer run time, just want to try with a list

        saved = set()

        for num in nums:
            if num in saved:
                return True
            saved.add(num)

        return False
