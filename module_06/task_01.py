import time
from threading import Thread

def get_thread(thread_name):
	time.sleep(1)
	print(f'start {thread_name}')

def gen_threads(n):
	list_thread = ["thread " + str(i + 1) for i in range(n)]
	return list_thread

n = 10
list_thread = gen_threads(n)

threads = [Thread(target = get_thread, args=(n, )) for n in list_thread]

for t in threads:
	t.start()

for t in threads:
	t.join()
