#import asyncio
#from googletrans import Translator
#
#msg = "Tarjima uchun so'z kiriting (chiqib ketish uchun \"q\" deb yozing): "
#
#
#async def main():
#    tarjimon = Translator()
#    while True:
#        text = input(msg)
#        if text == "q":
#            break
#        else:
#            tarjima = await tarjimon.translate(text, src='uz', dest='fr')
#            print(tarjima.text)
#
#
#asyncio.run(main())
import re

import requests
from bs4 import BeautifulSoup

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
r.raise_for_status()          # sahifa ochilmasa (404, 500...) shu yerda xato beradi

soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())

# Yangilik havolalari: /news/2026/09/21/... ko'rinishida bo'ladi
news = []
korilgan = set()
for a in soup.find_all('a', href=True):
    if not re.match(r'^/news/\d{4}/', a['href']):
        continue
    if a['href'] in korilgan:
        continue
    sarlavha = a.find(['h1', 'h2', 'h3', 'h4'])
    if sarlavha is None:
        continue
    korilgan.add(a['href'])
    news.append({
        'sarlavha': sarlavha.get_text(strip=True),
        'havola': 'https://kun.uz' + a['href'],
    })

print(f"Topilgan yangiliklar soni: {len(news)}\n")
for i, yangilik in enumerate(news, start=1):
    print(i, yangilik['sarlavha'])
    print('  ', yangilik['havola'])

print(news[3].text)