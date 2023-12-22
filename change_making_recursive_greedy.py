import sys
import time

# Recursive solution
def recursive_change_making(n, k, d):
    if n == 0:
        return [], 0
    if n < 0:
        return None, float('inf')
    
    min_coins = float('inf')
    best_coins = None

    for i in range(k):
        coin = d[i]
        remaining_coins, remaining_min = recursive_change_making(n - coin, k, d)
        
        if remaining_coins is not None and remaining_min + 1 < min_coins:
            min_coins = remaining_min + 1
            best_coins = remaining_coins + [coin]
    
    return best_coins, min_coins

# Greedy Algorithm solution
def greedy_change_making(n, k, d):
    coins_used = []
    i = k - 1
    
    while n > 0 and i >= 0:
        while n >= d[i]:
            coins_used.append(d[i])
            n -= d[i]
        i -= 1
    
    return coins_used, len(coins_used)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python change_making_recursive_greedy.py <n> <k> <d1 d2 ... dk>")
        sys.exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2])
    d = list(map(int, sys.argv[3].split()))

    start_time = time.time()
    recursive_result, recursive_time = recursive_change_making(n, k, d)
    end_time = time.time()

    print("Recursive Solution Result:")
    print(recursive_result)
    print("Time taken (nanoseconds):", end_time - start_time)

    start_time = time.time()
    greedy_result, greedy_time = greedy_change_making(n, k, d)
    end_time = time.time()

    print("\nGreedy Algorithm Result:")
    print(greedy_result)
    print("Time taken (nanoseconds):", end_time - start_time)
