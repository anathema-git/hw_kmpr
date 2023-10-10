
from get_data import get_data
import convector
from writer import writer


url = "https://www.dns-shop.ru/catalog/17a89d9b16404e77/veb-kamery/?order=6&q=веб%20камера&stock=now-today-tomorrow-later-out_of_stock"

headers = {
    "cookie": "PHPSESSID=561850639d10d16269e6fbec40d09051; _ab_=%7B%22search-sandbox%22%3A%22default%22%2C%22catalog-hit-filter%22%3A%22filtr_hit_default%22%7D; _gid=GA1.2.1227305482.1696889407; rrpvid=350195801064709; _gcl_au=1.1.276577209.1696889407; rcuid=65247a3ffe0a4d45a91530ca; cartUserCookieIdent_v3=1fa3aaaf39a4c1a878aa53eab76e88cf0146ada8676c8fae5f27fd6038be784ea%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22f2aadf2b-75a1-3115-82ec-a0e9648b0451%22%3B%7D; phonesIdentV2=77ba4677-f3a1-4e5a-800d-5ec518e16c56; _ym_uid=1678381255924865574; _ym_d=1696889410; tmr_lvid=87f588e71226d2d1455541c2ac394eb6; tmr_lvidTS=1696883264686; _ab_1_=333; _ym_isad=1; current_path=605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; lang=ru; _csrf=cb34122b61089133dceeb64a321152ed00c1611039153a8b6457bf3b889fcdc5a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22xJ_dnWPlj4JkJMvEm8WSabrPYhPaZqBS%22%3B%7D; city_path=moscow; qrator_jsid=1696952565.250.NrBg29bjKoYBtO4f-e2kt2v1ejt3i63pgtvd59bislhnj277d; _gat=1; _gat_%5Bobject%20Object%5D=1; _ym_visorc=b; _ga_FLS4JETDHW=GS1.1.1696952594.10.1.1696954872.47.0.0; tmr_detect=1%7C1696954872515; _ga=GA1.2.1200866557.1696889407; _gat_UA-8349380-2=1; _ga_YT23VHSRDB=GS1.2.1696952583.8.1.1696954885.39.0.0"
}

data = get_data(url, headers)
if data:
    data = convector.convector(data)
writer(data)