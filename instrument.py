from pyinstrument import Profiler
import time

# pyinstrument test

def slow(N=10):
    total = 0
    for i in range(N):
        total += i
        print(total)
        time.sleep(4)
    print('Slow done')
    print('-------------------')
    return total


def medium(N=10):
    total = 0
    for i in range(N):
        total += i
        print(total)
        time.sleep(2)
    print('Medium done')
    print('-------------------')
    return total


def fast(N=10000000):
    total = 0
    for i in range(N):
        total += i
    print(total)
    print('Fast done')
    print('-------------------')
    return total


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
    profiler = Profiler()
    profiler.start()
    main()
    profiler.stop()
    print(profiler.output_text(unicode=True, color=True))
