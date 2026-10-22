class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ref_image = image[sr][sc]

        def paint(row,col,visited):
            rows , cols = len(image) , len(image[0])

            if (min(row,col) < 0 or row == rows or col == cols or image[row][col] != ref_image or (row,col) in visited) or image[row][col] == color:
                return 

            image[row][col] = color 
            

            paint(row + 1,col,visited)
            paint(row - 1,col,visited)
            paint(row,col + 1,visited)
            paint(row,col - 1,visited)

            visited.add((row,col))

        paint(sr,sc,set())

        return image 
        