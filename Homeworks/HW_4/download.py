import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time


def download_images(url, approach, start_time):
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')
        os.makedirs(f'download_images_{approach}', exist_ok=True)
        img_tags = soup.find_all('img')

        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                img_url = urljoin(url, img_url)
                img_name = os.path.basename(urlparse(img_url).path)
                img_path = os.path.join(f'download_images_{approach}', img_name)

                with open(img_path, 'wb') as img_file:
                    img_file.write(requests.get(img_url).content)

                print(f'Изображение скачано: {img_name} за {time.time() - start_time:.2f} сек.')
    else:
        print(f'Ошибка при получении страницы. Код статуса: {response.status_code}')
