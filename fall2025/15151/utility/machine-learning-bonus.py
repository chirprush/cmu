from math import sqrt, log

l = [0]
N = 100

def f(x):
    return (1 + sqrt(1 + 4 * x * x)) / 2

for _ in range(N - 1):
    lt = f(l[-1])

    l.append(lt)

for s in range(1, N):
    for t in range(s, N):
        assert((l[s] / l[t]) ** 2 <= s / t)

# Surely I just need to prove this then hahahahahhaah
for t in range(N - 1):
    assert((l[t] / l[t + 1]) ** 2 <= t / (t + 1))
