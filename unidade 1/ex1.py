A = int(input())
B = int(input())

if A > 0 and B < 100 and B > A:
    for n in range(A, B, 2):
        print(n)
