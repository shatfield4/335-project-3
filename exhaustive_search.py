def soccer_opponent_avoidance(F, k):
    r, c = len(F), len(F[0])
    n = r + c - 2
    counter = 0
    for bits in range(0, 2**n):
        candidate = []
        for i in range(n):
            if (bits & (1 << i)):
                candidate.append('R')
            else:
                candidate.append('D')
        i, j = 0, 0
        avoid = set()
        for move in candidate:
            if move == 'R':
                j += 1
            else:
                i += 1
            if (i,j) in avoid:
                break
            if i >= r or j >= c or F[i][j] == 'X':
                break
            if F[i][j] == 'O':
                for a in range(max(0, i-k), min(r, i+k+1)):
                    for b in range(max(0, j-k), min(c, j+k+1)):
                        avoid.add((a,b))
        else:
            counter += 1
    return counter



if __name__ == "__main__":
    F = [['.', '.', '.', '.', '.', 'X', 'X', '.'],
     ['X', '.', '.', '.', '.', '.', '.', '.'],
     ['.', '.', 'X', '.', '.', 'X', '.', '.'],
     ['.', 'X', '.', '.', '.', 'X', '.', '.'],
     ['.', '.', '.', 'X', '.', '.', '.', '.'],
     ['.', '.', '.', '.', '.', '.', '.', '.'],
     ['.', '.', 'X', '.', 'X', '.', '.', '.'],
     ['.', '.', '.', '.', '.', '.', 'X', '.']]
    k = 1
    result = soccer_opponent_avoidance(F, k)
    print(result)

