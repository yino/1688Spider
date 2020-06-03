import json
import pandas as pd


def dis_res_json():
    with open('./res.json', mode="r", encoding="utf-8") as f:
        data = f.read()
    data = json.loads(data)

    company_name = []
    mobile = []
    desc = []
    address = []
    create_time = []
    register_money = []
    manage_scope = []
    for val in data:
        for v in val:
            company_name.append(v['company_name'])
            mobile.append(v['mobile'])
            desc.append(v['desc'])
            address.append(v['address'])
            create_time.append(v['create_time']['value']+'  '+v['create_time']['is_auth'])
            register_money.append(v['register_money']['value']+'  '+v['register_money']['is_auth'])
            manage_scope.append(v['manage_scope']['value']+'  '+v['manage_scope']['is_auth'])


    dataframe = pd.DataFrame({
        '公司名称': company_name,
        '电话': mobile,
        '简介': desc,
        '地址': address,
        '创建时间': create_time,
        '注册资金': register_money,
        '营业范围': manage_scope,
    })
    dataframe.to_csv('./data.csv', index=False)

def dis_company_info_text():
    with open('./test_company_info.txt', mode="r", encoding="utf-8") as f:
        data = f.read()
    data = data.replace('\'', '"')
    data = data.split('\n')
    company_name = []
    company_type = []
    company_province = []
    company_city = []
    company_reg_capital = []
    company_credit_level_text = [] #信用级别
    company_shop_repurchase_rate = [] #回购率
    credit_level_url = [] #诚信档案
    detail_url = [] #详情url

    for val in data:
        print(val)
        item = json.loads('%s' % (val, ))
        company_name.append(item['company_name'])
        company_type.append(item['company_type'])
        company_province.append(item['company_province'])
        company_city.append(item['company_city'])
        company_reg_capital.append(str(item['company_reg_capital'])+str(item['company_reg_unit']))
        company_credit_level_text.append(item['company_credit_level_text'])
        company_shop_repurchase_rate.append(item['company_shop_repurchase_rate'])
        credit_level_url.append(item['credit_level_url'])
        detail_url.append(item['detail_url'])

    dataframe = pd.DataFrame({
        '公司名称': company_name,
        '公司类型': company_type,
        '省': company_province,
        '市': company_city,
        '注册资金': company_reg_capital,
        '信用级别': company_credit_level_text,
        '回购率': company_shop_repurchase_rate,
        '信用详情地址': credit_level_url,
        '公司详情地址': detail_url,
    })
    dataframe.to_csv('./data/电子秤.csv', index=False)
    print(data)
    exit()

def dis_company_info_json(filename="电子秤"):
    with open('./data/%s.json' % (filename, ), mode="r", encoding="utf-8") as f:
        data = f.read()
    data = json.loads(data)
    company_name = []
    company_type = []
    company_province = []
    company_city = []
    company_reg_capital = []
    company_credit_level_text = [] #信用级别
    company_shop_repurchase_rate = [] #回购率
    credit_level_url = [] #诚信档案
    detail_url = [] #详情url
    goods_name = []
    goods_url = []
    for val in data:
        for v in val:
            item = v
            goods_name.append(item['goods_name'] if 'goods_name' in v.keys() else '',)
            goods_url.append(item['detail_url'] if 'detail_url' in v.keys() else '',)
            company_name.append(item['company_name'])
            company_type.append(item['company_type'])
            company_province.append(item['company_province'])
            company_city.append(item['company_city'])
            company_reg_capital.append(str(item['company_reg_capital'])+str(item['company_reg_unit']))
            company_credit_level_text.append(item['company_credit_level_text'])
            company_shop_repurchase_rate.append(item['company_shop_repurchase_rate'])
            credit_level_url.append(item['credit_level_url'])
            detail_url.append(item['detail_url'])

    dataframe = pd.DataFrame({
        '商品名称': goods_name,
        '商品详情地址': goods_url,
        '公司名称': company_name,
        '公司类型': company_type,
        '省': company_province,
        '市': company_city,
        '注册资金': company_reg_capital,
        '信用级别': company_credit_level_text,
        '回购率': company_shop_repurchase_rate,
        '信用详情地址': credit_level_url,
        '公司详情地址': detail_url,
    })
    dataframe.to_csv('./data/%s.csv' % (filename, ), index=False)
if __name__ == '__main__':
    keywordsList = [
        {
            "keyword": '理疗灯',
            "page": 40,
        },
        {
            "keyword": '冷热敷产品',
            "page": 13,
        },
        {
            "keyword": '口腔清洁',
            "page": 50,
        },
        {
            "keyword": '牙齿美白',
            "page": 50,
        },
        {
            "keyword": '除毛工具',
            "page": 50,
        },
        {
            "keyword": '直发棒',
            "page": 50,
        },
        {
            "keyword": '卷发棒',
            "page": 50,
        },
        {
            "keyword": '假睫毛',
            "page": 50,
        },
    ]
    for val in keywordsList:
        print(val['keyword'])
        dis_company_info_json(filename=val['keyword'])
