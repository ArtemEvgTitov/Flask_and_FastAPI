import asyncio
import aiohttp
import time
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

urls = [
    'https://codenamecrud.ru',
    'https://store.steampowered.com/app/814380/Sekiro_Shadows_Die_Twice__GOTY_Edition/',
    'https://www.python.org/',
    'https://ya.ru', ]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if response.status == 200:

                soup = BeautifulSoup(await response.read(), 'html.parser')
                os.makedirs(f'download_images_async', exist_ok=True)
                img_tags = soup.find_all('img')

                for img_tag in img_tags:
                    img_url = img_tag.get('src')
                    if img_url:
                        img_url = urljoin(url, img_url)
                        img_name = os.path.basename(urlparse(img_url).path)
                        img_path = os.path.join(f'download_images_async', img_name)

                        with open(img_path, 'wb') as img_file:
                            img_file.write(requests.get(img_url).content)

                        print(f'Изображение скачано: {img_name} за {time.time() - start_time:.2f} сек.')
            else:
                print(f'Ошибка при получении страницы. Код статуса: {response.status}')


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
