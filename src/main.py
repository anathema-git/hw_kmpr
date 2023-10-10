
from get_data import get_data
import convector
from writer import writer


url = "https://www.dns-shop.ru/catalog/17a89d9b16404e77/veb-kamery/?order=6&q=веб%20камера&stock=now-today-tomorrow-later-out_of_stock"

headers = {
    "cookie": "PHPSESSID=561850639d10d16269e6fbec40d09051; _ab_=%7B%22search-sandbox%22%3A%22default%22%2C%22catalog-hit-filter%22%3A%22filtr_hit_default%22%7D; _gid=GA1.2.1227305482.1696889407; rrpvid=350195801064709; _gcl_au=1.1.276577209.1696889407; rcuid=65247a3ffe0a4d45a91530ca; cartUserCookieIdent_v3=1fa3aaaf39a4c1a878aa53eab76e88cf0146ada8676c8fae5f27fd6038be784ea%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22f2aadf2b-75a1-3115-82ec-a0e9648b0451%22%3B%7D; phonesIdentV2=77ba4677-f3a1-4e5a-800d-5ec518e16c56; _ym_uid=1678381255924865574; _ym_d=1696889410; tmr_lvid=87f588e71226d2d1455541c2ac394eb6; tmr_lvidTS=1696883264686; _ab_1_=333; _ym_isad=1; current_path=605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; lang=ru; _csrf=52177822e91772b44b4030ad9e2e8ae49f1d994ff57f884fc67811737e8de64aa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22IBsyIvvqa1gCy-weZfxGVB780-J-2t4m%22%3B%7D; city_path=moscow; _ga_FLS4JETDHW=GS1.1.1696905209.6.1.1696905216.53.0.0; tmr_detect=1%7C1696905216726; _ga=GA1.2.1200866557.1696889407; _ga_YT23VHSRDB=GS1.2.1696905215.5.0.1696905229.46.0.0; qrator_jsr=1696907019.712.1Me8yGAX1Y91gwed-4i661u6t9agiq23adb11i8qqdpp0umtq-00; qrator_jsid=1696907019.712.1Me8yGAX1Y91gwed-cuatlsmhcd5a2rra3a11hscv2p6bg0ls"
}

data = get_data(url, headers)
if data:
    data = convector.convector(data)
writer(data)