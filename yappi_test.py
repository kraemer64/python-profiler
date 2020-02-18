import yappi
import time
import os


# generating yappi stats document
def yappi_write():
    yappi.stop()
    print('[YAPPI STOP]')
    # stats = yappi.get_func_stats()
    # threadstats = yappi.get_thread_stats()

    f = open("yappistats.txt", "a")

    # Configuratable stats output
    f.write('Functionstats\n')
    for stat in yappi.get_func_stats():
        f.write('Name: ' + stat.full_name + ' Ncall: ' + str(stat.ncall) + ' Ttot: ' + str(stat.ttot) + ' ')
        f.write('Module: ' + str(stat.module) + ' Children: ' + str(stat.children) + ' Tag: ' + str(stat.tag) + '\n')

    f.write('-------------------------------------------------------------------------------------\n')
    f.write('Threadstats\n')
    for threadstat in yappi.get_thread_stats():
        f.write('ID: ' + str(threadstat.id) + ' Name: ' + threadstat.name + ' Ttot: ' + str(threadstat.ttot) + ' Schedule: ' + str(threadstat.sched_count) + '\n')

    print(yappi.get_func_stats().print_all())
    f.close()

    # yappi.get_func_stats().debug_print()
    yappi.get_thread_stats().print_all()


# yappi test
def slow(N=10):
    total = 0
    for i in range(N):
        total += i
        #print(total)
        time.sleep(4)
    print('Slow done')
    print('-------------------')
    return total


def medium(N=10):
    total = 0
    for i in range(N):
        total += i
        #print(total)
        time.sleep(2)
    print('Medium done')
    print('-------------------')
    return total


def fast(N=10000000):
    total = 0
    for i in range(N):
        total += i
    #print(total)
    print('Fast done')
    print('-------------------')
    return total


def pythonic(N=10000000):
    total = sum(range(N))
    #print(total)
    print('Pythonic done')
    print('-------------------')
    return total


def main():
    fast()
    pythonic()
    medium()
    slow()


if __name__ == '__main__':
    print('[YAPPI START]')
    yappi.set_clock_type('wall')
    yappi.start()
    main()
    yappi_write()
