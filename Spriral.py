def spiral_order(matrix):
    result = []
    
    while matrix:
        # Append the first row
        result += matrix.pop(0)
        
        # Append the last element from each remaining row
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        
        # Append the last row in reverse order
        if matrix:
            result += matrix.pop()[::-1]
        
        # Append the first element from each remaining row in reverse order
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    
    return result



n=int(input())
matrix=[]
for i in range(n):
    matrix.append[input().split()]


spiral_result = spiral_order(matrix)
print(spiral_result)  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
