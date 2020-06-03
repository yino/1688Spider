#-*- encoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
import re
import asyncio
import aiohttp
import urllib.parse
loop = asyncio.get_event_loop()




class Spider:

    cookie = ''
    headers = {}
    session = ''
    def __init__(self):
        self.cookie = '__wpkreporterwid_=50a0056e-d33c-4bcf-09f1-2b9b2f4f37ce; _uab_collina=158797679880843135917049; cna=BQ4rFghTB1YCASvg1DiFJo8j; UM_distinctid=171a07e41f84b4-0525690f2fbaf4-404f012d-1fa400-171a07e41f98f1; taklid=4ce8438b6b5d44dd9ec32b5ad8911c5d; ali_beacon_id=106.36.219.175.1587535696848.453509.4; lid=sk%E5%A4%8F%E5%A4%A9%E7%88%B1%E7%82%AB%E8%88%9E; ali_apache_track=c_mid=b2b-2450174430|c_lid=sk%E5%A4%8F%E5%A4%A9%E7%88%B1%E7%82%AB%E8%88%9E|c_ms=1; ali_ab=1.86.247.179.1587956565228.8; h_keys="%u7535%u5b50%u79e4#%u9422%u975b%u74d9%u7ec9%ufffd#%u4e66%u5305"; t=f6057355837fcb991f41f901f22c2fb7; cookie2=1a1836d7a0975ed49a6761e01bd94c96; _tb_token_=fb0eeee811630; alicnweb=touch_tb_at%3D1588040547087%7Clastlogonid%3Dsk%25E5%25A4%258F%25E5%25A4%25A9%25E7%2588%25B1%25E7%2582%25AB%25E8%2588%259E%7Cshow_inter_tips%3Dfalse; cookie1=WqbzCtcEdFQa0HfjIxnV7LgCFSTd7n4ABpNj2cd2yxM%3D; cookie17=UUwVZGavdOMPBg%3D%3D; sg=%E8%88%9E07; csg=92de8d0b; unb=2450174430; uc4=nk4=0%40EoxbY%2B2CF5FuYLEczVBSq4VqHWsB2b0%3D&id4=0%40U27KCNZJRdM84%2FxPzAChLWwA54sS; __cn_logon__=true; __cn_logon_id__=sk%E5%A4%8F%E5%A4%A9%E7%88%B1%E7%82%AB%E8%88%9E; ali_apache_tracktmp=c_w_signed=Y; _nk_=sk%5Cu590F%5Cu5929%5Cu7231%5Cu70AB%5Cu821E; last_mid=b2b-2450174430; _csrf_token=1588040600617; _is_show_loginId_change_block_=b2b-2450174430_false; _show_force_unbind_div_=b2b-2450174430_false; _show_sys_unbind_div_=b2b-2450174430_false; _show_user_unbind_div_=b2b-2450174430_false; __rn_alert__=false; ad_prefer="2020/04/28 10:23:36"; l=eBrUAG7rQ2WBmGMDKO5w-urza7796IdfGsPzaNbMiIHca6dRGFZIuNQcq4nvPdtjgt5DTeKrOIii7RUX8SULRxsp8jGqj7hcoh96Se1..; isg=BGdnRPh89dkWXXFt93vJii_79psx7DvO5Qy3WznVc_YdKIPqQL1FHgNqSii2wBNG'
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://s.1688.com/selloffer/offer_search.htm/_____tmd_____/verify/?nc_token=3dc3b1b98b5cfeb7c0acc9660fb6eaf9&nc_session_id=01ucf0pUIPSXZXEL3kUQRUp4IkwU1tphT7-cNfTIGwfYNOLCjHixBqmyrbNhRHyGn8hODCdXewjUh5DV-9hutqEjIAubxgdpC_XVJIkYnRPSP219edBOcglOP2hiKzGEXk-sLAJKFB5UZI0rGQnTN_QQ&nc_sig=05L2PCzbBVsG-9sXw5odhWBZjynrbexKZ4gZD_UyQ9WV4PiTERwBEvX03v9hF-VfjiN25_Rj32uAx5U7Jt4Gk6dzimwx_-bSzU8pmNmlWdOGBI5-R_G0lS5pNSru5s5TGo6g_2d97Mna5dsa6Jc27scumomZbyGlJzFNPtiArH_dPycTQG_XsfT8eTcqvnikRlJbB6_wmYCz6FvIyZWNs9utaf2d8bZE_XpwTDh_vc7Ex3qxr2j_AqUwY4dvThRneoaHEG5uKEBtsCnGjrfNacrssBzUMsK165EDT6F8n9dyq-N1kKcc--nEMLKi4ERwCd8OZ9uxd2xzzdgL-L5K1jFcL1tncgE1fuCQcgk4eJwtLFreNxk8J9mGtLnw5nkywBpmQvOFg1n_tYHxBng4JfqQ&x5secdata=5e0c8e1365474455070961b803bd560607b52cabf5960afff39b64ce58073f78d3d7f9c6fdd165b15991bc1a196be81b4b5741360ad35dc9c497669d03d569efeb2bc16b1dbc91ea592f0222d32ec23f1976b91a091e5174a4153ee53f360b269783bbae415916f4e376d892cf8ccf5d07ae79ea43e8dbdaea58413aaa6c8f104f429a47db6e960f51275d67818a138c1495c5ea1c74aa3240030f9b698eb333b1b593d0e3b01362257e615d16192ffb6ac881b4e21bf92b0f699a17106371a5cf31ca34ff9d44d592136573dacfb1186367c2cd514be3c0e37ab638137d5120bc8156057807435e0b94f921d1e754f955a0d44cf476a595985ea90466f2c916bad3a334a270cce82b8e13bdb1dd65b155a76bfe9469b571da510edf6ff8f8acc20bb55cb85c8b452d9995b13105b90dc8a5376d5eeb10e4b18bc286a166d1630ba2afb0aa610bf7ac271d0799152c509d1cd5e1409f362e4405f9e739b15dcca26c1531222737cdcd5be2871ce012212f1689a3c3ad4ba7a73d63c6eb70bb5490b37d67b93a0f5dcb44f5cfd64896713ae399c31606b3ce3af23886c08b28ce970fe5e88c9ecc1040da793dc3617c8e1149ae8e03fac1bb2fd9b03377b2041759a80ee563c0dc09d098de56df83738790b2e0f74a85324cb4cfdd59c8daedbcfee2788e1213b5354113f2e798cf4ebf&x5step=100&nc_app_key=X82Y__4e04684f4bd5921802303555efd70b01',
            'upgrade-insecure-requests': '1',
            'cookie': self.cookie,
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        }

    def get_goods_detail(self, url):

        # headers = {
        #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        #     'accept-encoding': 'gzip, deflate, br',
        #     'accept-language': 'zh-CN,zh;q=0.9',
        #     'cache-control': 'max-age=0',
        #     'referer': 'https://kj.1688.com/',
        #     'upgrade-insecure-requests': '1',
        #     'cookie': self.cookie,
        #     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        # }
        # Response = requests.get(url=url, headers=headers, verify=False)
        #
        # with open('./goods_detail.html', mode="w+", encoding="utf-8") as f:
        #     f.write(Response.text)
        pass

    def get_company_info(self, url):
        Response = requests.get(url=url, headers=self.headers, verify=True)
        html = Response.text
        with open('./company_detail.html', mode="w+", encoding="utf-8") as f:
            f.write(html)
        # with open('./company_detail.html', mode="r", encoding="utf-8") as f:
        #     html = f.read()

        data = {}
        Html = etree.HTML(html)
        data['company_name'] = Html.xpath('.//div[@class="company-name"]/@title')[0]
        data['mobile'] = Html.xpath('.//span[@class="tip-info phone-num"]/text()')[0]
        data['desc'] = Html.xpath('.//p[@id="J_COMMON_CompanyInfoDetailInfo"]/span/text()')[0]
        value_data = Html.xpath('.//div[@class="info-box info-right"]/table/tr/td/p/span[@class="tb-value-data"]/text()')
        auth_data = Html.xpath('.//div[@class="info-box info-right"]/table/tr/td/p/span[@class="has-auth"]/text()')
        map_address = Html.xpath('.//a[@id="J_COMMON_CompanyInfoAddressMapBtn"]/@map-mod-config')[0]
        data['address'] = json.loads(map_address)['address']
        num = 0
        for val in value_data:
            if num == 0:
                data['create_time'] = {
                    'value': val,
                    'is_auth': auth_data[num],
                }
            if num == 1:
                data['register_money'] = {
                    'value': val,
                    'is_auth': auth_data[num],
                }
            if num == 2:
                data['manage_scope'] = {
                    'value': val,
                    'is_auth': auth_data[num],
                }
            num += 1

        print(data)
        exit()

    async def get_list(self, keywords, page=1):
        """
        async request get
        :param keywords: string
        :param page: int
        :return: string
        """
        url = 'https://s.1688.com/selloffer/offer_search.htm'
        params = {
            'keywords': keywords,
            'n': 'y',
            'netType': '1,11,16',
            'beginPage': page,
        }
        # Response = self.session.get(url=url, params=params, headers=self.headers)
        async with self.session.get(url=url, params=params, headers=self.headers) as Response:
            return await Response.text(encoding='utf8')

    def list_callback(self, content):
        """
        请求后的 call back
        :param content string
        """
        content = content.result()

        try:
            data = re.findall('window.data.offerresultData=successDataCheck\((.+?)\)', content)
            data = '%s' % (data[0],)
            data = json.loads(data)
            for val in data['data']['offerList']:
                name = val['information']['simpleSubject']
                detail_url = val['information']['detailUrl']
                content = "%s  %s\n" % (name, detail_url)
                with open('goods_list.txt', mode="a", encoding="utf-8") as f:
                    f.writelines(content)
                print(content)
        except BaseException as e:
            print('错误：', e)


    def test_list(self):

        Response = requests.get(url="https://s.1688.com/selloffer/offer_search.htm?keywords=电子秤&n=y&netType=1%2C11&encode=utf-8&spm=a260k.dacugeneral.search.0", headers=self.headers)
        content = Response.text
        with open('./list.html', encoding='utf-8', mode="w+") as f:
            f.write(content)
        data = re.findall('window.data.offerresultData=successDataCheck\((.+?)\)', content)
        data = '%s' % (data[0],)
        data = json.loads(data)
        print('len :', len(data['data']['offerList']))
        try:
            for val in data['data']['offerList']:
                name = val['information']['simpleSubject']
                detail_url = val['information']['detailUrl']
                content = "%s  %s\n" % (name, detail_url)
                # with open('goods_list.txt', mode="a", encoding="utf-8") as f:
                #     f.writelines(content)
                print(name)
        except BaseException as e:
            print('错误：', e)

    def url_gbk_parse(self, keywords):
        keywords = '电子秤'
        keywords = keywords.encode('gbk')
        keywords = urllib.parse.quote(keywords)
        return keywords

    def test(self):
        keywords = self.url_gbk_parse('电子秤')
        netType = self.url_gbk_parse('1,11,16')
        #获取request id
        url = 'https://s.1688.com/selloffer/offer_search.htm?keywords=%s&netType=%s' % (keywords, netType)
        Response = requests.get(url=url, headers=self.headers)
        content = Response.text
        pageConfig = re.findall('window.data.pageConfigData=successDataCheck\((.+?)\)', content)
        pageConfig = '%s' % (pageConfig[0],)
        pageConfig = json.loads(pageConfig)
        requestId = pageConfig['data']['requestId']

        #获取具体的内容 json
        url = 'https://search.1688.com/service/marketOfferResultViewService'
        data = {
            'keywords': keywords,
            'n': 'y',
            'netType': 16,
            'async': True,
            'asyncCount': 20,
            'beginPage': 2,
            'pageSize': 60,
            # 'requestId': requestId,
            'startIndex': 0,
            'offset': 8,
        }
        Response = requests.get(url=url, headers=self.headers, params=data)
        with open('./test.html', mode="w+", encoding='utf-8') as f:
            f.write(Response.text)



    def run(self):

        loop = asyncio.get_event_loop()
        self.session = aiohttp.ClientSession()
        tasks = []
        #
        # Response = self.get_list(keywords='电子秤', page=1)
        # listTask = asyncio.ensure_future(Response)
        # tasks.append(listTask)
        # # 回调
        # listTask.add_done_callback(self.list_callback)
        # loop.run_until_complete(asyncio.wait(tasks))
        # exit()
        for page in range(1, 50):
            Response = self.get_list(keywords='电子秤', page=page)
            listTask = asyncio.ensure_future(Response)
            tasks.append(listTask)
            # 回调
            listTask.add_done_callback(self.list_callback)
            # return listTask
        loop.run_until_complete(asyncio.wait(tasks))
        # exit()
        # #window.data.offerresultData = successDataCheck()
        #
        # # goods_url = "https://detail.1688.com/offer/565107076645.html?spm=a262gg.8864560.jqq32vsu.1.164b6510tPmJqF"
        # # self.get_goods_detail(url=goods_url)
        # company_url = 'https://gzcaiyoule.1688.com/page/creditdetail.htm'
        # self.get_company_info(url=company_url)
        # exit()

# async def hello(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             response = await response.text()
#             return response

if __name__ == '__main__':
    # tasks = []
    # url = "https://www.baidu.com/"
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(hello(url))
    #
    # exit()
    Spider = Spider()

    Spider.test()
    # Spider.run()
