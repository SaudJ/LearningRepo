from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

# Post = soup.findall('article')

# headline = Post.a.text

print(help(soup))










