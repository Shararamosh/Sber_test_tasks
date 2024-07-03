n, k = map(int, input("Введите количество банкоматов в данный момент (минус один) и количество новых банкоматов: ").split())
l = []
print("Введите расстояния между банкоматами в данный момент:")
for i in range(n):
    l.append((int(input()), 0))
min_dist = sum(i for i, _ in l)/(n+k)
for i in range(1, k+1):
    j_max = None
    s_max = None
    for j, t in enumerate(l):
        s = t[0]/(t[1]+1)
        if s_max is None or s > s_max:
            s_max = s
            j_max = j
    l[j_max] = (l[j_max][0], l[j_max][1]+1)
for t in l:
    for i in range(t[1]+1):
        print(t[0]/(t[1]+1))