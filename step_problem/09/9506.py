while True:
    N = int(input())
    if N == -1:
        break
    factors = [i for i in range(1, N) if N % i == 0]    # N을 제외한 약수들
    if N == sum(factors):
        print(f'{N} =', ' + '.join(map(str, factors)))
    else:
        print(f'{N} is NOT perfect.')
