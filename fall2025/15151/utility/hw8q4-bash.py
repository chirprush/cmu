count = 0

for a in range(6):
    for b in range(6):
        for c in range(6):
            for d in range(6):
                for e in range(6):
                    for f in range(6):
                        if len({a, b, c, d, e, f}) == 3:
                            count += 1

print(count)
