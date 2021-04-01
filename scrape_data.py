import requests
from bs4 import BeautifulSoup

url = "https://www.etsy.com/uk/listing/772695061/brass-or-silver-leaf-bookmark-set"

html_code = requests.get(url)

soup = BeautifulSoup(html_code.content, 'lxml')

product_name = soup.find('div', class_='wt-display-flex-lg wt-flex-direction-column-md wt-flex-lg-3 wt-pl-md-4 wt-pr-md-4 wt-pl-lg-0 wt-pr-lg-5 wt-pl-xs-2 wt-pr-xs-2')\
            .find("div", class_="wt-mb-xs-2").find("h1",class_="wt-text-body-03 wt-line-height-tight wt-break-word wt-mb-xs-1").get_text().strip()

print(product_name)

product_price = soup.find("div", class_="wt-display-flex-lg wt-flex-direction-column-md wt-flex-lg-3 wt-pl-md-4 wt-pr-md-4 wt-pl-lg-0 wt-pr-lg-5 wt-pl-xs-2 wt-pr-xs-2")\
                .find("div", class_="wt-display-flex-xs wt-align-items-center").find("p",class_="wt-text-title-03 wt-mr-xs-2").get_text().strip()

product_price = product_price[1:]


print(product_price)
