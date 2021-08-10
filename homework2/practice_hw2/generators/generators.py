import math


def prime_num():
    nm = 2

    while True:
        sq = math.ceil(nm ** 1 / 2)
        for i in range(2, sq + 1):
            if (nm % i) == 0:
                break
        else:
            yield nm
        nm += 1


print(prime_num())


for num in prime_num():
    print(num)
