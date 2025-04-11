A, B, C = map(int, input().split())
p = (A+B)%C
f1 = (A%C + B%C)%C
m = (A*B)%C
f2 = (A*B)%C
print(f'{p}\n{f1}\n{m}\n{f2}')