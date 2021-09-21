import time
from threading import Thread

def get_thread(thread_name):
	time.sleep(1)
	print(f'start {thread_name}')

threads = [Thread(target = get_thread, args=(n, )) for n in ['thread 1', 'thread 2', 'thread 3', 'thread 4', 'thread 5']]

for t in threads:
	t.start()

for t in threads:
	t.join()