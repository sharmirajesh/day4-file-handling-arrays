from collections import Counter, defaultdict

data = """Python is a cool language but OCaml
is even cooler since it is purely functional"""

result = defaultdict(lambda: [0, []])
for i, l in enumerate(data.splitlines()):
    for k, v in Counter(l.split()).items():
        result[k][0] += v
        result[k][1].append(i+1)

for k, v in result.items():
    print('{1} {0} {2}'.format(k, *v))
