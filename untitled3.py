import requests
import bs4

"https://books.toscrape.com/catalogue/page-2.html"

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')

print(soup.select(".product_pod"))
