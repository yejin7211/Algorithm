n = int(input())

fn = 0
f0 = 0
f1 = 1
for i in range(2, n + 1):
    fn = f0 + f1
    f0 = f1
    f1 = fn

if n == 0:
    print(f0)
elif n == 1:
    print(f1)
else: print(fn)

