from functools import reduce, wraps


def custom_cache(times=3):
    cache = dict()

    def wrapper(f):
        @wraps(f)
        def substitute(*args):
            if args in cache:
                cache[args][1] -= 1
                if cache[args][1] == 0:
                    print("Restored and deleted from cache")
                    return cache.pop(args)[0]
                print("Restored from cache")
                return cache[args][0]
            else:
                result = f(*args)
                print("Evaluated")
                cache[args] = [result, times]
                return result

        return substitute

    return wrapper


@custom_cache(times=4)
def summarize(*args):
    return reduce(lambda x, y: x + y, args)


print(summarize(1, 2, 3))
print(summarize(1, 2, 3))
print(summarize(1, 2, 3))
print(summarize(1, 2, 3))
print(summarize(1, 2, 3))
print(summarize(1, 2, 3))
print(summarize(1, 2, 3))
