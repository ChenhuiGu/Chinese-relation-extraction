'''
1。根据id得到公告文本
2。参数:id
3.分界点：1891498
'''
import json
import os
import re
from baidu_config import bd_client
# base_dir = os.path.split(os.path.realpath(__file__))[0]
from uuid import uuid1



def id2filepath(id):
    '''
    :param id:
    :return: file path
    '''
    base_dir = '/data01/guchh/df-copy'
    id = int(id)
    if id < 300000 or 700000 <= id < 1300000:
        dir = str(id % 60)
        dirpath = os.path.join(base_dir, dir)
    elif id>1891489:
        dir = str(id % 200)
        dirpath = os.path.join(base_dir, dir)
    else:
        dir = str(id % 70)
        dirpath = os.path.join(base_dir, dir)
    filepath = dirpath + '/%d.txt'%id
    return filepath


def get_define_entity():
    '''
    1。位于'第一节释义'和' 第二节  公司简介和主要财务指标'之内的词作为实体识别源
    2。分词，过滤
    '''
    exclude_word = ['会', '局', '院', '部', '委', '所', '盟', '国']
    with open('company_list.csv') as f0:
        companys = f0.readlines()
    f1 = open('train_data.csv','a')
    for company in companys[1:]:
        name,code,id = tuple(company.strip().split(','))
        filepath = id2filepath(id)
        with open(filepath) as f2:
            lines = f2.readlines()
        for line in lines:
            if '第二节  公司简介和主要财务指标' in line:
                break
            line = line.lstrip().rstrip()
            if line:
                entities = baidu_segmentation(line)
                if entities:
                    entitie = entities[0]
                    print(entitie)
                    if entitie[-1] not in exclude_word:
                        # sentences = re.findall(r'.{50}%s.{50}' % entitie, content)
                        f1.write('%s,%s'%(name,entitie))
    f1.close()



def baidu_segmentation(query):
    '''对query进行词性标注,抽取机构实体和名词'''
    if query is None or len(query) == 0:
        return []
    entities = []
    query = query.encode('gbk', errors='ignore').decode('gbk')
    items = []
    response = bd_client.lexer(query)
    if 'error_code' not in response:
        items = items + response['items']
    else:
        print('error baidu nlp response: %s' % response)
    for item in items:
        if item['ne'] == 'ORG':
            entities.append(item['item'])
    return entities

if __name__ == '__main__':
    get_define_entity()