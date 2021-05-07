def has_word(y, x, word, board):
    def in_range(y, x):
        if y < 0 or y >= 5 or x < 0 or x >= 5:
            return False
        else:
            return True
    
    if not in_range(y, x):
        return False

    if board[y][x] != word[0]:
        return False

    if len(word) == 1:
        return True

    dx = [-1, -1, -1, 1, 1, 1, 0, 0]
    dy = [-1, 0, 1, -1, 0, 1, -1, 1]
    for d in range(8):
        ny, nx = y+dy[d], x+dx[d]
        if has_word(ny, nx, word[1:], board):
            return True
    
    return False

if __name__ == '__main__':
    n_test = int(input())

    while n_test:
        board = []
        for _ in range(5):
            board.append(list(input()))

        n_word = int(input())
        words = []
        for _ in range(n_word):
            words.append(list(input()))

        for word in words:
            exist = any([has_word(i, j, word, board) for i in range(5) for j in range(5)])
            ret = 'YES' if exist else 'NO'
            print('%s %s'%(''.join(word), ret))
        
        n_test -= 1