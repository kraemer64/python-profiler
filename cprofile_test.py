import cProfile
import time
import pstats

# cProfile test
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
    #medium()
    #slow()

if __name__ == '__main__':
    #main()
    print('Direktes Profiling--------------')
    cProfile.run('main()', 'restats.txt)
    print('Direktes Profiling closed--------------')
    print('')
    print('Ausgelagertes Profiling----------')
    cProfile.run('main()', 'restats.txt')
    restats = pstats.Stats('restats.txt')
    restats.strip_dirs().sort_stats(-1).print_stats()
    print('Ausgelagertes Profiling done----------')
