a = int(input())
m = int(input())
if not 1 <= a <= 50 or not 1 <= m <= 50:
    exit()
elif a + m > 50:
    print("N")
else:
    print("S")