# balanced character

A string is considered "balanced" when every letter in the string appears both in uppercase and lowercase. For e.g., CATattac is balanced (a, c, t occur in both cases), while Madam is not (a, d only appear in lowercase). Write a function that, given a string, returns the shortest balanced substring of that string. For e.g.,:
“azABaabza” should return “ABaab”
“TacoCat” should return -1 (not balanced)
“AcZCbaBz” should returns the entire string

# Get Raidus

My application has this resolution width of 1080 pixels, height of 1920 pixels. I use the camera preview, its resolution is width 1920, and height 1080. Then I process the touch on the screen, get the coordinates for example x = 250, and y = 600. Then there is some processing using the camera preview frames. But not everything is as it should be. I think this is due to the difference in resolution parameters. How to change the width and height of the places? Then I draw a rectangle on the new coordinates, which are calculated based on the old ones, but they are too different and not even close to the result.

참고: https://stackoverflow.com/questions/54599521/how-to-calculate-pixel-position

# cleaning robots

Question 2: Robot Room Cleaner
There is a cleaning robot which is cleaning a rectangular grid of size Nx M, represented by array R consisting of N strings. Rows are numbered from 0 to N-1 (from top to bottom) and columns are numbered from 0 to M-1 (from left to right).

The robot starts cleaning in the top-left corner, facing rightwards. It moves in a straight line for as long as it can, i.e. while there is an unoccupied grid square ahead of it. When it cannot move forward, it rotates 90 degrees clockwise and tries to move forward again until it encounters another obstacle, and so on. Dots in the array (".") represent empty squares and 'x's represent occupied squares (ones the robot cannot move through). Each square that the robot occupied at least once is considered clean. The robot moves indefinitely.

Write a function:

int solution (vector &R);

that, given an array R consisting of N strings, each of length M, representing the grid, returns the number of clean squares.

Examples:

Given A = [...X..","..XX","..X..."], your function should return 6.
image

참고: https://leetcode.com/discuss/interview-question/1373943/microsoft-oa-sde-2

# magic square

A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

Example 1:

Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.

- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12
  Example 2:

Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
Output: 2

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 106

참고: https://leetcode.com/problems/largest-magic-square/
참고: https://leetcode.com/problems/largest-magic-square/discuss/1267544/Python%3A-Explained-Easy%3A-Check-all-Squares.
