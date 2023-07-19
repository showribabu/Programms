''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
"""
def ind(l,e):
    v=[]
    for z in l:
        for s in z:
            if s==e:
                v.append(f'{(l.index(z))+1}#{(z.index(s))+1}')
    return v
                
            


def main():
    # Write code here
    N=int(input())
    l=[]
    for i in range(N):
        x=list(map(int,input().split('#')))
        l.append(x)
    l1=[]
    for x in l:
        l1.append(max(x))
    e=max(l1)
    e1=ind(l,e)
    for i in e1:
        print(i)


main()
"""
"""
def get_neighboring_indexes(grid, row, col):
    num_rows = len(grid)
    num_cols = len(grid[0])
    neighboring_indexes = []

    # Define the possible directions around the block
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for dx, dy in directions:
        new_row = row + dx
        new_col = col + dy

        # Check if the neighboring indexes are within the grid boundaries
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            neighboring_indexes.append((new_row, new_col))

    return neighboring_indexes


def find_neighboring_indexes(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    result = []

    for row in range(num_rows):
        for col in range(num_cols):
            neighboring_indexes = get_neighboring_indexes(grid, row, col)
            result.append((row, col, neighboring_indexes))

    return result


grid = [
    [12, 45, 33, 27],
    [94, 54, 23, 53],
    [98, 59, 27, 62],
    [11, 51, 67, 13]
]

neighboring_indexes = find_neighboring_indexes(grid)
for index in neighboring_indexes:
    print(index)
"""
#########################################3
def find_max_min_positions(grid):
    n = len(grid)
    max_min_amount = 0
    positions = []

    # Iterate through each block in the grid
    for i in range(n):
        for j in range(n):
            min_amount = float('inf')
            
            # Consider all neighboring blocks
            for x in range(max(0, i-1), min(n, i+2)):
                for y in range(max(0, j-1), min(n, j+2)):
                    amount = grid[x][y]
                    min_amount = min(min_amount, amount)
            
            # Update maximum minimum amount and positions
            if min_amount > max_min_amount:
                max_min_amount = min_amount
                positions = [(i+1, j+1)]
            elif min_amount == max_min_amount:
                positions.append((i+1, j+1))
    
    # Convert positions to string format
    positions_str = [f"{x}#{y}" for x, y in positions]
    
    return positions_str

def main():
    # Read grid size
    n = int(input())

    # Read grid values
    grid = []
    for _ in range(n):
        row = list(map(int, input().split('#')))
        grid.append(row)

    # Find positions that maximize minimum amount
    max_min_positions = find_max_min_positions(grid)

    # Print the positions
    for position in max_min_positions:
        print(position)

if __name__ == "__main__":
    main()

####################3
1. The `find_max_min_positions` function takes in the grid as input and returns a list of positions that will maximize the minimum amount your friend can win.

2. In the `main` function, the grid size `n` is read from the input.

3. The grid values are then read from the input and stored in a 2D list called `grid`.

4. The `find_max_min_positions` function is called with the grid as an argument, and the returned list of positions is stored in the variable `max_min_positions`.

5. Finally, the positions are printed one by one in the desired format.

Now, let's go through the implementation of the `find_max_min_positions` function:

1. The function takes in the grid as input and initializes the variables `n`, `max_min_amount`, and `positions`.

2. The nested `for` loops iterate through each block in the grid.

3. For each block, a variable `min_amount` is initialized to infinity. This variable will keep track of the minimum amount that your friend can win by considering all neighboring blocks.

4. The nested `for` loops iterate through the neighboring blocks of the current block. The `max` and `min` functions are used to handle boundary cases and ensure that the indices are within the grid boundaries.

5. The amount on the current neighboring block is compared with the current `min_amount`, and if it is smaller, the `min_amount` is updated.

6. After considering all the neighboring blocks, the `min_amount` represents the minimum amount that your friend can win if they choose the current block.

7. The `min_amount` is then compared with the current `max_min_amount`. If it is greater, the `max_min_amount` is updated and the list of positions `positions` is cleared and a new position (i+1, j+1) is added.

8. If the `min_amount` is equal to the `max_min_amount`, the current position (i+1, j+1) is added to the list of positions.

9. Finally, the list of positions is converted to the desired string format (x#y) and returned.

