class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)

        ## just reverse the string and track the spaces

        whitespace_found = False
        alphabet_count = 0

        for i in range(n - 1, -1, -1):
            if s[i] == ' ' and not whitespace_found: continue
            if s[i] == ' ' and whitespace_found:
                break
            else:
                alphabet_count += 1
                whitespace_found = True

        return alphabet_count