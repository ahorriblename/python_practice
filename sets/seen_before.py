num_sequence = input().split()
num_sequence = map(int, num_sequence)

seen = set()

for num in num_sequence:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)