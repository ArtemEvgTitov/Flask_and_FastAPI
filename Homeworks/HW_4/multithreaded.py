import threading
import time
from download import download_images

urls = [
    'https://codenamecrud.ru',
    'https://store.steampowered.com/app/814380/Sekiro_Shadows_Die_Twice__GOTY_Edition/',
    'https://www.python.org/',
    'https://ya.ru', ]

threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download_images, args=[url, 'multithreaded', start_time])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
