print('--- 1o exemplo ---')
i = 1
while i < 6:
  print(i)
  i += 1

print('--- 2o exemplo ---')
j = 0
while j < 10:
    print(j)
    j += 1
    if j == 5:
        break
    else:
        continue

print('--- 3o exemplo ---')
k = 1
while k < 6:
    print(k)
    k += 1
else:
    print('k não é mais menor do que 6.')