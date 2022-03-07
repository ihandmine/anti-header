from anti_header import Header
from pprint import pprint
import anti_header


if __name__ == '__main__':
    # hd = Header(platform='windows', min_version=90, max_version=100).base
    # hd = Header(platform='windows', min_version=90, max_version=100).random
    # print(anti_header.VERSION)

    # must_header param useage
    # hd = Header(must_header={'aa': 'bb'}).random
    # hd = Header(must_header={'aa': 'bb'}).base

    # rand_header param useage
    hd = Header(url='https://www.baidu.com/', rand_header={'cc': 'dd'}).random
    # hd = Header(rand_header={'cc': 'dd'}).base
    pprint(hd.to_unicode_dict())

    # default_header param useage
    # for i in range(10):
    #     hd = Header(default_header={'ee': 'ff'}).base
    #     pprint(hd.to_unicode_dict())

