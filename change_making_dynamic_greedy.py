import sys
import time

# Top Down Dynamic Programming solution
def dynamic_change_making(n, k, d):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        for j in range(k):
            if i >= d[j]:
                dp[i] = min(dp[i], dp[i - d[j]] + 1)
    
    coins_used = []
    remaining = n
    while remaining > 0:
        for j in range(k):
            if remaining >= d[j] and dp[remaining] == dp[remaining - d[j]] + 1:
                coins_used.append(d[j])
                remaining -= d[j]
                break
    
    return coins_used, dp[n]

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
        print("Usage: python change_making_dynamic_greedy.py <n> <k> <d1 d2 ... dk>")
        sys.exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2])
    d = list(map(int, sys.argv[3].split()))

    start_time = time.time()
    dynamic_result, dynamic_time = dynamic_change_making(n, k, d)
    end_time = time.time()

    print("Dynamic Programming Result:")
    print(dynamic_result)
    print("Time taken (nanoseconds):", end_time - start_time)

    start_time = time.time()
    greedy_result, greedy_time = greedy_change_making(n, k, d)
    end_time = time.time()

    print("\nGreedy Algorithm Result:")
    print(greedy_result)
    print("Time taken (nanoseconds):", end_time - start_time)
