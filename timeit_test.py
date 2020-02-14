import time
import timeit

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed

# timeit test
@timeit
def slow(N=10):
    total = 0
    for i in range(N):
        total += i
        print(total)
        time.sleep(4)
    print('Slow done')
    print('-------------------')
    return total


@timeit
def medium(N=10):
    total = 0
    for i in range(N):
        total += i
        print(total)
        time.sleep(2)
    print('Medium done')
    print('-------------------')
    return total


@timeit
def fast(N=10000000):
    total = 0
    for i in range(N):
        total += i
    print(total)
    print('Fast done')
    print('-------------------')
    return total


@timeit
def pythonic(N=10000000):
    total = sum(range(N))
    print(total)
    print('Pythonic done')
    print('-------------------')
    return total


def main():
    fast()
    pythonic()
    medium()
    slow()

if __name__ == '__main__':
    main()
