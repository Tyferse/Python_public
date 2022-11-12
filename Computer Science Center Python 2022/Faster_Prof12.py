import cProfile
import line_profiler


if __name__ == '__main__':
    source = open('Faster12.py').read()
    cProfile.run(source, sort='tottime')

    L = line_profiler.LineProfiler()
    L.run("bench()").print_stats()

