import time
from threading import Thread

def get_thread(thread_name):
	time.sleep(1)
	print(f'start {thread_name}')

threads_names = ['thread 1', 'thread 2', 'thread 3', 'thread 4', 'thread 5']
threads = [Thread(target = get_thread, args=(n, )) for n in threads_names]

for t in threads:
	t.start()

for t in threads:
	t.join()