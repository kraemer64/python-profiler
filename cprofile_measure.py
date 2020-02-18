import cProfile
import pstats

# writing cProfile data into cmd
def profileprint(profiler):
    print('\n<---------CMD Function Profiling--------->\n')
    p = pstats.Stats(profiler)
    p.strip_dirs().sort_stats(-1).print_stats()

# cProfile decorator
def profileit(func):
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        retval = profiler.runcall(func, *args, **kwargs)
        profileprint(profiler)
        return retval
    
    return wrapper
