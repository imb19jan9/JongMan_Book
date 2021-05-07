def set(board, y, x, type, delta):
    coverType = [
        [[0,0],[1,0],[0,1]],
        [[0,0],[0,1],[1,1]],
        [[0,0],[1,0],[1,1]],
        [[0,0],[1,0],[1,-1]]
        ]

    ok = True
    for i in range(3):
        ny = y + coverType[type][i][0]
        nx = x + coverType[type][i][1]
        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
            ok = False
        else:
            board[ny][nx] += delta
            if board[ny][nx] > 1:
                ok = False
    return ok

def cover(board):
    y, x = None, None
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                y, x = i, j
                break
        if y is not None:
            break

    if y is None:
        return 1
    
    ret = 0
    for type in range(4):
        if set(board, y, x, type, 1):
            ret += cover(board)
        set(board, y, x, type, -1)
    return ret
    
if __name__ == '__main__':
    n_test = int(input())
    
    while n_test:
        h, w = list(map(int, input().split()))
        board = []
        cnt = 0
        for _ in range(h):
            board.append([1 if ch == '#' else 0 for ch in input()])
            cnt += board[-1].count(0)

        if cnt%3 != 0:
            print('0')
            continue

        print('%d'%(cover(board)))
        n_test -= 1