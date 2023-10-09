#pip install requests, beautifulsoup4, lxml
import requests
from bs4 import BeautifulSoup

url = "https://www.dns-shop.ru/catalog/17a89d9b16404e77/veb-kamery/?order=6&q=веб%20камера&stock=now-today-tomorrow-later-out_of_stock"

headers = {
    "cookie": "qrator_jsr=1696889405.131.yJDxSPQrj3UzThpZ-dqrr8mhg4kcq6i8m74s6drbcntlaehhk-00; qrator_jsid=1696889405.131.yJDxSPQrj3UzThpZ-spa4a93rn3va3fe4qqhsnur8m2euotbf; lang=ru; city_path=moscow; PHPSESSID=561850639d10d16269e6fbec40d09051; _ab_=%7B%22search-sandbox%22%3A%22default%22%2C%22catalog-hit-filter%22%3A%22filtr_hit_default%22%7D; current_path=75a2da2a93c8cd1c2e00f91901d024508daafdcdf99566e6de24aeb998c59557a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A114%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22geoip%22%7D%22%3B%7D; _csrf=1873189f8be9f0105a2b28c2d83bbc81832463d899b5cc90119dd0206c9d521ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22bak3z8iEr_FqCQhWhiU2WEpJDYvHuX6-%22%3B%7D; _gid=GA1.2.1227305482.1696889407; rrpvid=350195801064709; _gcl_au=1.1.276577209.1696889407; rcuid=65247a3ffe0a4d45a91530ca; cartUserCookieIdent_v3=1fa3aaaf39a4c1a878aa53eab76e88cf0146ada8676c8fae5f27fd6038be784ea%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22f2aadf2b-75a1-3115-82ec-a0e9648b0451%22%3B%7D; phonesIdentV2=77ba4677-f3a1-4e5a-800d-5ec518e16c56; _ym_uid=1678381255924865574; _ym_d=1696889410; tmr_lvid=87f588e71226d2d1455541c2ac394eb6; tmr_lvidTS=1696883264686; _ga_FLS4JETDHW=GS1.1.1696889269.3.1.1696889410.55.0.0; _ab_1_=333; _ym_isad=1; _ym_visorc=b; tmr_detect=0%7C1696889414349; _ga=GA1.2.1200866557.1696889407; _ga_YT23VHSRDB=GS1.2.1696889411.1.0.1696889422.49.0.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "lxml") # html.parser

    data = soup.find("div", class_="catalog-product ui-button-widget")

    item = data.find("a", class_="catalog-product__name ui-link ui-link_black")

    name = item.find("span")

    print(name)

else:
    print(response.status_code)