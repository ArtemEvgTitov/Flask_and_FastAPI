from multiprocessing import Process
import time
from download import download_images

urls = [
    'https://codenamecrud.ru',
    'https://store.steampowered.com/app/814380/Sekiro_Shadows_Die_Twice__GOTY_Edition/',
    'https://www.python.org/',
    'https://ya.ru', ]

processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download_images, args=(url, 'multiprocess', start_time))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
