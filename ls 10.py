n = int(input("введите количество монет: "))
k = 0
for i in range(n):
    v = int(input("введите 0, если мнетка лежит ввер орлом, 1, если решкой: "))
    if v == 1:
        k += 1
print(k if k < n / 2 else n-k)