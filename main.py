import requests
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
#print(r_html)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r_html,'html.parser')
#print(soup.prettify())
print(soup.title.name)
print(soup.title.string)
#title = soup.find('span', 'articletitle').string