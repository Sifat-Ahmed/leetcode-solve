class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        ## I will just try to do a char by char matching, with one loop
        if s == "" and t: return True
        if s and t == "": return False

        index = 0

        for i in range(len(t)):
            if index < len(s):
                if t[i] == s[index]:
                    index += 1

        if index != len(s):
            return False
        return True