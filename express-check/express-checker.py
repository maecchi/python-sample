#
# Japan SuperExpress Delay Cheker
#

#
import time
import requests
from bs4 import BeautifulSoup


def checkOperationInfo(url):
    """
    運行情報を確認し、運行情報を返却する

    Parameters
    ----------
    url : string
        運行情報対象URL
    """
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    og_desc = soup.find('meta', attrs={
        "property": "og:description", 'content': True})
    return (og_desc['content'])


def main():
    """
    main 関数
    """
    infos = []
    dict_transit_urls = {
        "北海道": "https://transit.yahoo.co.jp/traininfo/detail/637/0/",
        "東北": "https://transit.yahoo.co.jp/traininfo/detail/1/0/",
        "秋田": "https://transit.yahoo.co.jp/traininfo/detail/6/0/",
        "山形": "https://transit.yahoo.co.jp/traininfo/detail/5/0/",
        "上越": "https://transit.yahoo.co.jp/traininfo/detail/3/0/",
        "北陸": "https://transit.yahoo.co.jp/traininfo/detail/624/0/",
        "東海道": "https://transit.yahoo.co.jp/traininfo/detail/7/0/",
        "山陽": "https://transit.yahoo.co.jp/traininfo/detail/8/0/",
        "九州": "https://transit.yahoo.co.jp/traininfo/detail/410/0/"
    }
    for name, url in dict_transit_urls.items():
        description = checkOperationInfo(url)
        infos.append("{0:<5s}: {1}".format(name, description))
        time.sleep(1)

    # 一括表示
    for info in infos:
        print(info)


if __name__ == "__main__":
    main()
