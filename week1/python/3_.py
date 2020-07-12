from collections import defaultdict as dd


def check(time, q):
    p = queue.pop(0)
    q -= 1
    output.append(p)
    if p == -1:
        return check(time)
    else:
        return time+p


s, n = map(int, input().split())

a, p = map(int, input().split())

time = a+p

output = [a]

queue = []
q = 0

inputs = []

for _ in range(n - 1):
    inputs.append(tuple(map(int, input().split())))

at = set()
pt = dd(list)

for a, p in inputs:
    at.add(a)
    pt[a].append(p)

at = sorted(list(at))
if len(at) > 0:
    for t in range(max(at)+inputs[n-2][1]):
        if t in at:
            for p in pt[t]:
                if q < s:
                    queue.append(p)
                    q += 1
                else:
                    queue.append(-1)
        if t >= time:
            time = check(time, q)


for o in output:
    print(o)
