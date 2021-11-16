#!/usr/bin/env python
# coding: utf-8

# In[1]:


n,m=map(int,input().split())
a=*map(int,input().split()),
i=c=d=0
for x in map(int,input().split()):
  while c+a[i]<x:c+=a[i];d+=1;i+=1
  print(d+1,x-c)


# C:\Users\Vicky\Desktop\Repository\Algorithms\coding ninja\Code Kaze - Nov 2021\Hackathon>python solution.py
# 5 8
# 10 1 1 1 10
# 9 10 11 12 13 14 15 23
# 1 9
# 1 10
# 2 1
# 3 1
# 4 1
# 5 1
# 5 2
# 5 10
