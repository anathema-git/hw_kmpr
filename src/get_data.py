#pip install requests, beautifulsoup4, lxml
import requests
from bs4 import BeautifulSoup

def get_data(url, headers):

    def get_names(url, page):
        
        response = requests.get(url + "&p=" + str(page), headers=headers)

        if response.status_code == 200:

            result = []

            soup = BeautifulSoup(response.text, "lxml") # html.parser

            data = soup.find_all("div", class_="catalog-product ui-button-widget")

            for position in data:

                item = position.find("a", class_="catalog-product__name ui-link ui-link_black")

                name = item.find("span")

                result.append(name)

        else:
            print(response.status_code)
            return []

        return result

    names = []

    for page in range(1, 9):
        names += get_names(url, page)

    return names