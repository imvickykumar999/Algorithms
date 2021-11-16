#!/usr/bin/env python
# coding: utf-8

# In[ ]:


d = {}
n = int(input())
for _ in range(n-1):
    a, b = map(int, input().split())
    d[a] = d.get(a, 0) + 1
    d[b] = d.get(b, 0) + 1
zz = list(filter(lambda x: d[x] > 2, d))
z = len(zz)
y = list(filter(lambda x: d[x] == 1, d))
if z > 1:
    print("No")
elif z == 0:
    print("Yes")
    print(1)
else:
    print("Yes")
    print(len(y))


# C:\Users\Vicky\Desktop\Repository\Algorithms\coding ninja\Code Kaze - Nov 2021\Breakdown the tree>python solution.py
# 5
# 1 2
# 1 3
# 1 4
# 1 5
# Yes
# 4
