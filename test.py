import requests

url = f'https://kidkodschool.github.io/welcome.html'

response = requests.get(url)

# print(response.reason)

with open('./pyt_is_cool.html', 'wb') as f:
    f.write(response.content)