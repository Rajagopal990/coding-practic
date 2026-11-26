arr = input().split()

freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1

print("Repeating elements:")

for key, value in freq.items():
    if value > 1:
        print(key)