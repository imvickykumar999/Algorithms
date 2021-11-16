n = int(input())
a = [*map(int, input().strip())]
f = 0, *map(int, input().strip().split())
i = 0

while i < n and f[a[i]] <= a[i]:
    i += 1

while i < n and f[a[i]] >= a[i]:
    a[i] = f[a[i]]
    i += 1

print(*a, sep='')


# C:\Users\Vicky\Desktop\Repository\Algorithms\coding ninja\Code Kaze - Nov 2021\Ninja in Danger>python solution.py
# 4
# 1733
# 1 2 5 4 6 6 3 1 9
# 1755
