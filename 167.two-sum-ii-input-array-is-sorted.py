class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ## I have done 3 sum, 4 sum before. Also have the idea of 2 sum
        ## I need two pointers and the given array is already sorted
        ## if target > left + right then right --
        ## vice-versa left ++
        ## else soln

        left, right = 0, len(numbers) - 1

        while right > left:
            ## first checking if the result is found
            if numbers[left] + numbers[right] == target:
                ## don&t need to carry on, because there is only one soln
                return left + 1, right + 1

            ## in a sorted array, if sum is greater than target then we need to reduce sum, so we reduce right
            elif numbers[left] + numbers[right] > target:
                right = right - 1

            else:
                left = left + 1
