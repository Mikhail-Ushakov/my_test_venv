import requests
from bs4 import BeautifulSoup

#query = 'cats'
url = f'https://python-scripts.com/beautifulsoup-html-parsing#method-find-all'

page = requests.get(url).text

soup = BeautifulSoup(page, 'html.parser')

# with open('test_requests.html', 'wb') as f:
#     f.write(soup)

for imge in soup.find_all('a'):
    link = imge.get('href')
    if link and link.startswith('https'):
        # response = requests.get(link)
        with open('linki.txt', 'a') as f:
            f.write(link + '\n')
        