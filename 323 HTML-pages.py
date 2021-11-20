from bs4 import BeautifulSoup
import requests
import sys

url1 = input()
url2 = input()

page1 = requests.get(url1)
soup1 = BeautifulSoup(page1.text, "html.parser")
page1urls = soup1.findAll('a')
urls = []

for i in range(len(page1urls)):
    url = page1urls[i].get('href')
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    urls.extend(soup.findAll('a'))

for i in range(len(urls)):
    urls[i] = urls[i].get("href")
    if url2 == urls[i]:
        print("Yes")
        sys.exit()

print("No")
