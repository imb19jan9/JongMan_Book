def count_pairings(n, taken, are_friends):
    first_free = None
    for i in range(n):
        if not taken[i]:
            first_free = i
            break

    if first_free is None:
        return 1
    
    ret = 0
    for pair_with in range(first_free+1, n):
        if not taken[pair_with] and are_friends[first_free][pair_with]:
            taken[first_free], taken[pair_with] = True, True
            ret += count_pairings(n, taken, are_friends)
            taken[first_free], taken[pair_with] = False, False

    return ret

if __name__ == '__main__':
    n_test = int(input())
    while n_test:
        n_people, n_friends = list(map(int, input().split()))
        taken = [False] * n_people
        are_friends = [[False]*n_people for _ in range(n_people)]
        friends = list(map(int, input().split()))
        for i in range(n_friends):
            i, j = friends[2*i], friends[2*i+1]
            are_friends[i][j], are_friends[j][i] = True, True
        
        print(count_pairings(n_people, taken, are_friends))
        n_test -= 1
