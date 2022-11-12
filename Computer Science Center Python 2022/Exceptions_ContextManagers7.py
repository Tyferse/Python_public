import contextlib
import functools
import io
import os
import tempfile
import threading
import traceback
# from urllib.request import urlopen


p = 42

try:
    1/0
except ZeroDivisionError as e:
    p = e

print(p)

print(*[e.__name__ for e in BaseException.__subclasses__()])
print(*[e.__name__ for e in Exception.__subclasses__()])

"""
AssertionError
ImportError
NameError
AttributeError
KeyError
IndexError
ValueError
TypeError
"""


class TestFailure(Exception):
    def __str__(self):
        return 'Lecture test failed'


try:
    raise TestFailure
except TestFailure as e:
    traceback.print_tb(e.__traceback__)
    print(e)

"""
try:
    {}['foo']
except KeyError as e:
    raise RuntimeError('Oops!') from e
"""

"""
  File "C:\Program Files\Python\
  CSC Python 2022\Exceptions_ContextManagers7.py", line 34, in <module>
    raise TestFailure
Traceback (most recent call last):
  File "C:\Program Files\Python\CSC Python 2022\
  Exceptions_ContextManagers7.py", line 41, in <module>
    {}['foo']
KeyError: 'foo'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Program Files\Python\CSC Python 2022\
  Exceptions_ContextManagers7.py", line 43, in <module>
    raise RuntimeError('Oops!') from e
RuntimeError: Oops!
"""

try:
    print('hi')
except Exception:
    pass
else:
    # 'foobar'.split('')
    pass
finally:
    print('End!')


"""
with acquire.resource() as r:
    do_something(r)
    

manager = acquire.resource()
r = manage.__enter__()
try:
    do_something(r)
finally:
    exc_type, exc_value, tb = sys.xc_info()
    suppress = manager.__exit__(exc_type, exc_value, tb)
    if exc_value is not None and not suppress:
        raise exc_value
        

with acquire.resource() as r, acquire.other_resource() as other:
    do_something(r, other)
    

with acquire.resource() as r:
    with acquire.other_resource() as other:
        do_something(r, other)
"""


class opened:
    def __init__(self, path, *args, **kwargs):
        self.opener = functools.partial(open, path, *args, **kwargs)

    def __enter__(self):
        self.handle = self.opener()
        return self.handle

    def __exit__(self, *exc_info):
        self.handle.close()
        del self.handle


with opened('example2.txt', mode='wt') as handle:
    handle.write('Context manager was there!')


with tempfile.TemporaryFile() as handle:
    path = handle.name
    print(path)

"""
print(open(path))
Traceback (most recent call last):
  File "C:\Program Files\Python\CSC Python 2022\
  Exceptions_ContextManagers7.py", line 125, in <module>
    print(open(path))
FileNotFoundError: [Errno 2] No such file or directory: 
'C:\\Users\\Dom\\AppData\\Local\\Temp\\tmpms8ubpuy'
"""


class synchronized:
    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        self.lock.acquire()

    def __exit__(self, *exc_info):
        self.lock.release()


with synchronized():
    print('Всё, что здесь происходит, имеет только один поток '
          'и не больше одного')


class cd:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.saved_cmd = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, *exc_info):
        os.chdir(self.saved_cmd)


print(os.getcwd())

# with cd('/tmp'):
#     print(os.getcwd())


"""
url = 'http://compscicenter.ru'
with contextlib.closing(urlopen(url)) as page:
    print(page)
"""

handle = io.StringIO()
with contextlib.redirect_stdout(handle):
    print('Hello, world!')

print(handle.getvalue())

with contextlib.suppress(FileNotFoundError):
    os.remove('example3.txt')


class Supress:
    def __init__(self, *suppressed):
        self.suppressed = suppressed

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, tb):
        return (exc_type is not None
                and issubclass(exc_type, self.suppressed))


class suppressed(contextlib.suppress, contextlib.ContextDecorator):
    pass


@suppressed(IOError)
def do_something():
    pass


"""
def merge_logs(output_path, *logs):
    handles = open_files(logs)
    with open(output_path, 'wt') as output:
        merge(output, handles)
    close_files(logs)


def merge_logs(output_path, *logs):
    with contextlib.ExitStack() as stack:
        handles = [stack.enter_context(open(log)) for log in logs]
        output = open(output_path, 'wt')
        stack.enter_context(output)
        merge(output, handles)
"""
