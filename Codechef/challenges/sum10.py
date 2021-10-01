
# lst = [2,4,3,1,7,11,5]
lst = [7,9,3,5,3,1,5]

s = set()
sum = 10
res = []

for i in range(len(lst)):
    temp = sum-lst[i]

    if (temp in s) and str(lst[i]) != str(temp):
        res.append((lst[i], temp))
    s.add(lst[i])

print(set(res))
