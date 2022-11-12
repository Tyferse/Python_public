import asyncio
# import collections
import concurrent.futures as ft
import math
# import multiprocessing as mp
# import queue
import threading
import time
from functools import partial
from joblib import Parallel, delayed
# from urllib.request import urlretrieve


def countdown(n):
    for i in range(n):
        print(n - i - 1, 'left')
        time.sleep(1)


t = threading.Thread(target=countdown, args=(3, ))
t.start()


class CountDownThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):  # вызывается методом start
        for i in range(self.n):
            print(self.n - i - 1, 'left')
            time.sleep(1)


t = CountDownThread(3)
print(t.name)
t.start()
print(t.ident)


t = threading.Thread(target=time.sleep, args=(4, ))
t.start()
t.join()
t.join()


t = threading.Thread(target=time.sleep, args=(4, ))
t.start()
print(t.is_alive())
time.sleep(4)
print(t.is_alive())


t = threading.Thread(target=time.sleep, args=(4, ), daemon=True)
t.start()
t.daemon


class Task:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n < 5:
            n += 1
            yield n


class SharedCounter:
    def __init__(self, value):
        self._value = value
        self._lock = threading.Lock()

    def increment(self, delta=1):
        self._lock.acquire()  # захватывает примитив синхронизации
        self._value += delta
        self._lock.release()  # отдаёт примитив синхронизации

    def get(self):
        return self._value


done = threading.Lock()


def idle_release():
    print('Running')
    time.sleep(5)
    done.release()


print(done.acquire())
threading.Thread(target=idle_release).start()
done.acquire() and print('WAT?')


"""
q = collections.deque()
is_empty = threading.Condition()


def producer():
    while 1:
        is_empty.acquire()  # всё, что между acquire и release
        q.append(something)  # попадает в один поток
        is_empty.notify()
        is_empty.release()


def consumer():
    while True:
        is_empty.acquire()
        while not q:
            is_empty.wait()
            
        something = q.popleft()
        is_empty.release()


def follow(connection, connection_lock, q):
    try:
        while True:
            connection_lock.acquire()
            message = connection.read_message()
            connection_lock.release()
            q.put(message)
            
    except InvalidMessage:
        follow(connection, connection_lock, q)


follower = threading.Thread(target=follow, args=something)
follower.start()
"""


def follow(connection, connection_lock, q):
    try:
        while True:
            with connection_lock:
                message = connection.read_message()
                
            q.put(message)
            
    except IOError:
        follow(connection, connection_lock, q)


"""
queue.Queue  # collections.deque
queue.LifoQueue  # list
queue.PriorityQueue  # list


def worker(q):
    while True:
        item = q.get()  # блокирует и ожидает следующий элемент
        do_something(item)
        q.task_done()  # уведомляет очередб о выполнении задания


def master(q):
    for item in source():
        q.put(item)
    
    # блокирует и ожидает, пока все элементы очереди не будут обработаны
    q.join()
"""

executor = ft.ThreadPoolExecutor(max_workers=4)
print(executor.submit(print, 'Hello World'))
print(list(executor.map(print, ['Knock?', 'Knock!'])))
executor.shutdown()

with ft.ThreadPoolExecutor(max_workers=4) as executor:
    f = executor.submit(sorted, [4, 3, 1, 2])
    print(f.running(), f.done(), f.cancelled())
    print(f.result(), f.exception(), sep='\n')
    f.add_done_callback(print)


def integrate(f, a, b, *, n_iter=1000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step

    return acc


print(integrate(math.cos, 0, math.pi / 2))
print(integrate(math.sin, 0, math.pi))


def integrate_async(f, a, b, *, n_jobs, n_iter=1000):
    executor = ft.ThreadPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, integrate, f,
                    n_iter=n_iter // n_jobs)

    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step)
          for i in range(n_jobs)]
    return sum(func.result() for func in ft.as_completed(fs))


print(integrate_async(math.cos, 0, math.pi / 2, n_jobs=2))
print(integrate_async(math.sin, 0, math.pi, n_jobs=2))

"""
 GIL (global interpreter lock) - это мьютекс, который гарантирует, 
что в каждый момент времени только один поток имеет доступ 
к внутреннему состоянию интерпретатора.


with ft.ThreadPoolExecutor(max_workers=4) as executor:
    with open('urls.txt', 'r') as handle:
        for url in handle:
            executor.submit(urlretrieve, url)
"""


async def echo(source, target):
    while True:
        line = await source.readline()
        if not line:
            break
            
        target.write(line)


loop = asyncio.get_event_loop()
server = asyncio.start_server(echo, port=8080)
loop.create_task(server)


"""
try:
    loop.run_forever()
finally:
    server.close()
    loop.close()



p = mp.Process(target=countdown, args=(3, ))
p.start()
print(p.name, p.pid, p.daemon)
p.join()
print(p.exitcode)


def ponger(conn):
    conn.send('pong')


parent_conn, child_conn = mp.Pipe()
P = mp.Process(target=ponger, args=(child_conn, 1))
P.start()
parent_conn.recv()
p.join()
"""


def integrate_async(f, a, b, *, n_jobs, n_iter=1000):
    executor = ft.ProcessPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, integrate, f,
                    n_iter=n_iter // n_jobs)

    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step)
          for i in range(n_jobs)]
    return sum(func.result() for func in ft.as_completed(fs))


print(integrate_async(math.cos, 0, math.pi / 2, n_jobs=2))
print(integrate_async(math.sin, 0, math.pi, n_jobs=2))


def integrate_async(f, a, b, *, n_jobs, n_iter=1000, backend=None):
    step = (b - a) / n_jobs
    with Parallel(n_jobs=n_jobs, backend=backend) as parallel:
        fs = (delayed(integrate)(a + i * step, a + (i + 1) * step,
                                 n_iter=n_iter // n_jobs)
              for i in range(n_jobs))
        return sum(parallel(fs))


print(integrate_async(math.cos, 0, math.pi / 2, n_jobs=2))
print(integrate_async(math.sin, 0, math.pi, n_jobs=2))
