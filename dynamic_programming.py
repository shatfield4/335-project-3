# Names:
# Trenton Coggeshall
# Sean Hatfield
# Malik Hidouk


def soccer_dyn_prog(F):
    r, c = len(F), len(F[0])

    # Corner case: initial cell is impassible
    if F[0][0] == 'X':
        return 0

    A = [[0 for x in range(c)] for y in range(r)]

    # Base case
    A[0][0] = 1
    # General cases
    for i in range(r):
        for j in range(c):
            if F[i][j] == 'X':
                A[i][j] = 0
                continue
            above = left = 0
            if i > 0 and F[i - 1][j] == '.':
                above = A[i - 1][j]
            if j > 0 and F[i][j - 1] == '.':
                left = A[i][j - 1]
            A[i][j] += above + left

    return A[r - 1][c - 1]






if __name__ == "__main__":
    F = [['.', '.', '.', '.', '.', '.', 'X', '.', 'X'],
     ['X', '.', '.', '.', '.', '.', '.', '.', '.'],
     ['.', '.', '.', 'X', '.', '.', '.', 'X', '.'],
     ['.', '.', 'X', '.', '.', '.', '.', 'X', '.'],
     ['.', 'X', '.', '.', '.', '.', 'X', '.', '.'],
     ['.', '.', '.', '.', 'X', '.', '.', '.', '.'],
     ['.', '.', 'X', '.', '.', '.', '.', '.', 'X'],
     ['.', '.', '.', '.', '.', '.', '.', '.', '.']]
    print("Dynamic programming result:", soccer_dyn_prog(F))
