f = lambda p : "\\textcolor{blue}{\\( \\checkmark \\)}" if p else "\\textcolor{red}{\\( \\times \\)}"
imp = lambda p, q: (not p) or q

for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            print(f"{f(p)} & {f(q)} & {f(r)} & {f(imp(p, q))} & {f(imp(p, r))} & {f(q or r)} & {f(imp(p, q) or imp(p, r))} & {f(imp(p, q or r))} \\\\")
