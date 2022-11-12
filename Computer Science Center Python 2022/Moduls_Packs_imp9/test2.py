import types
from useful import *
from importlib.util import find_spec
from importlib.util import module_from_spec


print(foo, boo())
with open('./useful.py') as handle:
    source = handle.read()

code = compile(source, 'useful.py', mode='exec')
print(exec(code, types.ModuleType('test1').__dict__))

print(find_spec('_useful_speedups'))

spec = find_spec('enum')
mod = spec.loader.create_module(spec)
print(mod)

mod = module_from_spec(spec)
print(mod)
spec.loader.exec_module(mod)
print(mod)
