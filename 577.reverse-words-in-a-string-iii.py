class Solution:
    def reverseWords(self, s: str) -> str:
        ## this one is interesting tbh, if I am not using library functions
        ## I will just try the one that hits my mind

        ## what I am thinking at the beginning is that I will iterate the sentance until I find a space
        ## once I find a space, that is my right pointer, and start position is my left pointer, now just do reverse
        ## once reverse is done, update the left pointer to current position and keep doing until the end

        left = 0
        result = ''
        for i in range(len(s)):
            ## if there is a space, take it as a substring and reverse
            ## but there is no space once the sentence if finished, for the last word
            if s[i] == ' ' or i == len(s) - 1:  # for the last word

                right = i if i == (len(s) - 1) else i - 1  # for both conditions space and last word

                while left <= right:
                    result += s[right]
                    right -= 1
                ## I also need to save the space and last alphabet because I am checking for i-1 for last word
                ## that means I am missing the last alphabet
                result += s[i] if i != (len(s) - 1) else ''

                ## update left for new word
                left = i + 1

        return result