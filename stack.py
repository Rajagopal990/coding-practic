stack = []

n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter element: "))
    stack.append(x)

print("Stack:", stack)

# Push
x = int(input("Enter element to push: "))
stack.append(x)
print("After Push:", stack)

# Pop
if len(stack) > 0:
    print("Popped element:", stack.pop())
else:
    print("Stack is empty")

# Peek
if len(stack) > 0:
    print("Top element:", stack[-1])

# Display
print("Final Stack:", stack)