arr = list(map(int, input().split()))

n = len(arr) + 1

total = n * (n + 1) // 2

list_sum = sum(arr)

print(total - list_sum)