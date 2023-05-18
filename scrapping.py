import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('scraped_data.db')
c = conn.cursor()


url = 'https://www.amazon.in/Apple-New-iPhone-12-128GB/dp/B08L5TNJHG/'

response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')


reviews = soup.find_all('div', {'data-hook': 'review'})

for review in reviews:
    title = review.find('a', {'data-hook': 'review-title'}).get_text().strip()
    text = review.find('span', {'data-hook': 'review-body'}).get_text().strip()
    style_name_element = review.find('a', {'data-hook': 'format-strip'})
    style_name = style_name_element.get_text().strip() if style_name_element else None

    color_element = review.find('a', {'data-hook': 'format-strip', 'title': 'Color Name'})
    color = color_element.get_text().strip() if color_element else None
    
    verified_purchase = review.find('span', {'data-hook': 'avp-badge-linkless'}).get_text().strip()


    c.execute('INSERT INTO reviews (title, text, style_name, color, verified_purchase) VALUES (?, ?, ?, ?, ?)', (title, text, style_name, color, verified_purchase))

conn.commit()

conn.close()
