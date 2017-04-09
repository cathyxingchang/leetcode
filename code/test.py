
tmp = []
q = 2.3
begin = 0
end = len(tmp)-1
position = None
while begin <= end:
    mid = (begin + end) / 2
    if tmp[mid] == q:
        position = mid
        break
    elif tmp[mid] > q:
        end = mid - 1
    else:
        begin = mid + 1
if position is None:
    if begin == -1:
        position = 0
    else:
        position = begin
print position
tmp.insert(position, q)
print tmp