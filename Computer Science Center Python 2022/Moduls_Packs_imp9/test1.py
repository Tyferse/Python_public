# import marshal
import sys
import time
import types
import useful


print(useful.foo)
useful.attr = 43
print(useful.attr)
# useful.__all__ = []
print(dir(useful))

print(types.ModuleType('test2'))

print(useful.__cached__)
handle = open(useful.__cached__, 'rb')


def read_int(hand):
    return int.from_bytes(hand.read(4), 'little')


magic = read_int(handle)
mtime = read_int(handle)
print(magic, mtime)
print(time.asctime(time.localtime()))
print(read_int(handle))
# print(marshal.loads(handle.read()))

print('useful' in sys.modules)
print(sys.modules['sys'])

print(sys.meta_path)
builtin_finder, _, path_finder = sys.meta_path
print(builtin_finder.find_spec('itertools'))  # встроенный (язык C)
print(path_finder.find_spec('enum'))  # модуль на python

spec = path_finder.find_spec('collections')
print(spec.name, spec.origin, spec.cached)
print(spec.parent, spec.submodule_search_locations, spec.loader)

print(sys.path_hooks)
