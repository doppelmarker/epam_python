a = [int(num) for num in input()]
a.sort()

new_arr = []
print(a)

i = 0
while i < len(a):
    local_count = 1
    try:
        while a[i] == a[i + 1]:
            i += 1
            local_count += 1
    except IndexError:
        pass
    if local_count > 1:
        new_arr.append(a[i])
    i += 1

print(new_arr)
