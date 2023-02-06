a = int(input())
l1 = int(input())
l2 = int(input())
hj = int(input())
lj = int(input())
if not 1 <= a <= 100 or not 1 <= l1 <= 100 or not 1 <= l2 <= 100 or not 1 <= hj <= 100 or not 1 <= lj <= 100:
    exit()
elif l1 * a <= hj * lj or l2 * a <= hj * lj:
    print("S")
else:
    print("N")
