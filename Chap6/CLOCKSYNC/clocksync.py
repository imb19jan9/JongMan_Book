def solve(clocks, swtch, linked):
    def are_aligend():
        for i in range(len(clocks)):
            if clocks[i] != 12:
                return False
        return True

    if swtch == 10:
        return 0 if are_aligend() else float('inf')
    
    def push():
        for i in linked[swtch]:
            clocks[i] = 3 if clocks[i] == 12 else clocks[i] + 3

    ret = float('inf')
    for cnt in range(4):
        ret = min(ret, cnt + solve(clocks, swtch+1, linked))
        push()
    return ret
    
if __name__ == '__main__':
    linked = [
        [0,1,2],
        [3,7,9,11],
        [4,10,14,15],
        [0,4,5,6,7],
        [6,7,8,10,12],
        [0,2,14,15],
        [3,14,15],
        [4,5,7,14,15],
        [1,2,3,4,5],
        [3,4,5,9,13]
        ]

    n_test = int(input())
    while n_test:
        clocks = list(map(int, input().split()))
        print(solve(clocks, 0, linked))    
        n_test -= 1