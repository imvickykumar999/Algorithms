#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline
for i in range(int(input())):
	n = int(input());g = [[] for i in range(n + 1)]
	for i in range(n - 1):u, v = map(int, input().split());g[u].append(v);g[v].append(u)
	i = 0;q = [1];p = [None] * (n + 1);w = [True] * (n + 1);r = 0
	while i < len(q):
		x = q[i];P = p[x];i += 1
		for v in g[x]:
			if v != P:q.append(v);p[v] = x
	for i in range(len(q) - 1, 0, -1):
		x = q[i];P = p[x];c = len([1 for v in g[x] if v != P and w[v]])
		if c != 0:r += c - 1;w[x] = False
	c = len([v for v in g[1] if w[v]])
	print(r + 1) if c == 0 else print(r + c)


# C:\Users\Vicky\Desktop\Repository\Algorithms\coding ninja\Code Kaze - Nov 2021\Ninja preparing for ICPC>python solution.py
# 1
# 6
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 2
