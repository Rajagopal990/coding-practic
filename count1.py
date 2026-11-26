# arr = [1, 2, 3, 2, 1, 4, 2, 3]
arr =  input().split()

freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key, value in freq.items():
    print(key, ":", value)