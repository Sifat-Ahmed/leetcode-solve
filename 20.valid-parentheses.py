class Solution:
    def isValid(self, s: str) -> bool:

        ## creating a stack to save the parentheses pair
        stack = []

        ## map for the parentheses pair
        ## for each key there is a valid closing parentheses
        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            ## if is a closing bracket
            if char in map.keys():
                ## save it in the stack
                stack.append(map[char])
            ## for closing bracket just check if its in the last position of the stack
            elif not stack or stack[-1] != char:
                return False
            else:
                stack.pop()

        return len(stack) == 0

if __name__ == '__main__':
    s = Solution()
    case = ["()", "()[]{}", "(({})[)]"]

    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.isValid(case[i])))