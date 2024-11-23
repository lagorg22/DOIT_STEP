import queue
import threading

def foo(q: queue.Queue[int]):
    while True:
        try:
            num = q.get(timeout=0.5)
            even_odd = 'Odd' if num % 2 else 'Even'
            thread_id = threading.get_ident()

            print(f'Thread ID: {thread_id}\n'
                  f'{num} is {even_odd}\n')
            q.task_done()
        except queue.Empty:
            break

q = queue.Queue()
threads = []

for _ in range(3):
    thread = threading.Thread(target=foo, args=(q,))
    thread.start()
    threads.append(thread)

for i in range(50):
    q.put(i)

for thread in threads:
    thread.join()

print('Everything done.')


