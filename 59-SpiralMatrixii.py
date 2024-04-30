from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # nums = [[0] * n for _ in range(n)]
        # startx, starty = 0, 0 #starting point for each loop
        # loop = n//2 #how many loops
        # mid = n//2 #the center position of the matrix
        # count = 1

        # for offset in range(1, loop + 1): #offset is the loop number that need to go thru
        #     for i in range(starty, n-offset): #left to right
        #         nums[startx][i] = count
        #         count += 1

        #     for i in range(startx, n-offset): #top to bottom
        #         nums[i][n-offset] = count
        #         count += 1

        #     for i in range(n-offset, starty, -1): #right to left
        #         nums[n-offset][i] = count
        #         count += 1

        #     for i in range(n-offset, startx, -1): #bottom to top
        #         nums[i][starty] = count
        #         count += 1

        #     startx += 1
        #     starty += 1

        
        # if n%2 != 0:
        #     nums[mid][mid] = count

        # return nums

    #another method
        if n <= 0:
            return []
        
        #initialise a base matrix
        List = [[0]* n for _ in range(n)]

        #initialise the starting point for each side and the starting value
        top, bottom, left, right = 0, n-1, 0, n-1
        count = 1

        while top <= bottom and left <= right:
            for i in range(left, right+1): #left to right
                List[top][i] = count
                count += 1
            top += 1

            for i in range(top, bottom+1): #top to bottom
                List[i][right] = count
                count += 1
            right -= 1

            for i in range(right, left-1, -1): #right to left
                List[bottom][i] = count
                count += 1
            bottom -= 1

            for i in range(bottom, top-1, -1): #bottom to top
                List[i][left] = count
                count += 1
            left += 1

        return List

n = 3

result = Solution().generateMatrix(n)
print(result)