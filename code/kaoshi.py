import sys

for line in sys.stdin:
    a = line.split()
    print int(a[0]) + int(a[1])
    n = int(a[0])
    L = int(a[1])

begin = 1
end = 2
maxLen = 101

nmid = (n + 1) << 1
a = -1
b = -1
nsum = begin + end
curLen = 101


def sum(num1, num2):
    sum = (num1 + num2) * (num2 - num1 + 1) / 2
    return sum


while begin < nmid:
    if nsum == n:
        if end - begin + 1 < maxLen and end - begin + 1 >= L and end - begin + 1 < curLen:
            curLen = end - begin + 1
            a = begin
            b = end
    while nsum > n and begin < nmid:
        nsum -= begin
        begin += 1
        if nsum == n:
            if end - begin + 1 < maxLen and end - begin + 1 >= L and end - begin + 1 < curLen:
                curLen = end - begin + 1
                a = begin
                b = end
    end += 1
    nsum += end

for i in range(a, b):
    print i,
print b