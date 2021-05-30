
import requests
from bs4 import BeautifulSoup  #to isolate data from the website

url = 'https://api.meteomatics.com/2018-01-01T14:10:00.000+00:00/t_2m:C/17.3887859,78.4610647/csv?model=mix'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')  #to isolate only the text sections with the tag 'span'
authors = soup.find_all('div', class_= 'tags')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quotesTags= tags[i].find_all('a', class_= 'tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)

