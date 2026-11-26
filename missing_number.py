arr = input().split()

n = len(arr)
total = n*(n+1) // 2
list_sum = sum(arr)

print(total - list_sum)