
import requests
from bs4 import BeautifulSoup  #to isolate data from the website

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')  #to isolate only the text sections with the tag 'span'

for quote in quotes:  #to remove the html elements remained in the text we just obtained
    print(quote.text)

