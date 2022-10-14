class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ## so as it says, if there is a parentheses that is not valid inside a big chain/str
        ## then the bigger side will be taken into account
        ## i.e. ()()())(((())))) -> invalid ()()()// valid -> (((())))) because longest withou any mistakes

        max_length = 0
        ## first we need a stack to save the index
        stack=[-1]

        for i in range(len(s)):
            ## if there is an opening bracket then hold the index
            if s[i] == '(':
                stack.append(i)
            else:
                ## if closing bracket, just pop the last inserted index
                stack.pop()
                ## if the stack is empty save the last index
                if not stack:
                    stack.append(i)
                else:
                    ## if not then get the maximum of previously found brackets vs currently found
                    max_length=max(max_length, i-stack[-1])
        return max_length

if __name__ == '__main__':
    s = Solution()
    haystack = ["(()", ")()())", "", "())))"]

    for i in range(len(haystack)):
        print('Test case {}: {} -> {}'.format(i+1, haystack[i], s.longestValidParentheses(haystack[i])))
