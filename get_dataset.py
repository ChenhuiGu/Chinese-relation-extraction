import codecs
import json
from uuid import uuid1
from baidu_config import bd_client
import re
import os
import Config


def get_file_path_list(root):
    '''得到root目录下的全部文件'''
    res = []
    for dir in os.listdir(root):
        dirpath = os.path.join(root, dir)
        if os.path.isdir(dirpath):
            for file in os.listdir(dirpath):
                if os.path.isfile(file):
                    res.append(os.path.join(dirpath, file))
        else:
            res.append(os.path.join(dirpath))
    return res


def get_notice_text(id):
    '''根据ID得到文本的内容'''
    pass


entity_list = []

def search_keyword(key, content, *args):
    '''
    1.在文本中获取关键词所在的句子
    2.获取距离关键词最近的entity
    3.拼接json，去重
    '''
    exclude_word = ['会', '局', '院', '部', '委', '所', '盟', '国','办','府']
    write_data = []
    # 重置
    global entity_list
    sentences = re.findall(r'.{50}%s.{50}' % key, content)
    tailword, relation = args

    for query in sentences:
        key_index = query.index(key)
        print(query)
        index = []
        # list
        entitys = baidu_segmentation(query)
        temp_dict = {
            "head": {},
            "relation": "",
            "sentence": "",
            "tail": {}
        }
        if entitys:
            if len(entitys)>1:
                for entity in entitys:
                    index.append(query.index(entity))
                tar_index = get_nearby(index,key_index)
                entitys = [entitys[tar_index]]

            if entitys[0] not in entity_list and entitys[0][-1] not in exclude_word:
                temp_dict["head"] = {
                    "word": entitys[0],
                    "id": str(uuid1())
                }
                temp_dict["tail"] = {
                    "word": tailword,
                    "id": str(uuid1())
                }
                temp_dict["sentence"] = ''.join(query)
                temp_dict["relation"] = relation

                write_data.append(temp_dict)
                entity_list.append(entitys[0])
    return write_data

def get_nearby(num,target):
    dis = []
    for i in num:
        dis.append(abs(target-i))
    tar_index = dis.index(max(dis))
    return tar_index

def get_train_data():
    '''获取训练集数据'''
    write_data = []
    key_words = {
        '持有股票': ['股票', '股东', '股权投资', '控股', '持有'],
        '合作': ['联合', '合作', '携手', '伙伴'],
        '关联': ['关联'],
        '担保': ['担保'],
        '供应商': ['供应', '供货', '提供', '竞标'],
        '客户': ['客户', '中标', '销售', '供应', '供货', '提供'],
        '子公司': ['子公司', '收购', '被收购'],
        '法律纠纷': ['法律纠纷', '中标'],
        '竞争对手': ['竞争对手'],
    }
    files = get_file_path_list(Config.TRAIN_DATA)
    for file in files:
        tailword = file.split('/')[-1][:-4]
        with open(file) as f:
            content = f.read()
        for relate in list(key_words.keys()):
            for key_word in key_words[relate]:
                print(key_word)
                write_data.extend(search_keyword(key_word, content, tailword, relate))
        write_file = Config.CN_DATA + tailword + '.json'
        with open(write_file, 'w') as f1:
            f1.write(json.dumps(write_data, ensure_ascii=False, indent=2))


def get_define_entity(filename):
    '''
    1。位于'定义'和'词汇表'之内的词作为实体识别源
    2。分词，过滤
    '''
    f1 = open('test.json', 'w')
    write_data = []
    with open(filename) as f:
        content = f.read().split('词汇表')
    # source = re.search(r'定义.*词汇表',content).group()
    entities = set(baidu_segmentation(content[2]))
    exclude_word = ['会', '局', '院', '部', '委', '所', '盟', '国']
    exit_entity = []
    for headword in entities:
        temp_dict = {
            "head": {},
            "relation": "",
            "sentence": "",
            "tail": {}
        }
        if headword[-1] not in exclude_word and len(headword) > 2:
            sentences = re.findall(r'.{50}%s.{50}' % headword, content[-1])

            # sentence = re.findall(r'[^。]*?{}[^。]*?。'.format(headword), content[-1])
            if 0 < len(sentences) < 10:
                sentence = ''.join(sentences)
                headword, tailword, relation, sentence = (headword, '中兴通讯', 'NA', sentence)

                if headword not in exit_entity:
                    temp_dict["head"] = {
                        "word": headword,
                        "id": str(uuid1())
                    }
                    temp_dict["tail"] = {
                        "word": tailword,
                        "id": str(uuid1())
                    }
                    temp_dict["sentence"] = ''.join(sentence)
                    temp_dict["relation"] = relation

                    write_data.append(temp_dict)
                    exit_entity.append(headword)
                    print(headword)

    f1.write(json.dumps(write_data, ensure_ascii=False, indent=2))
    f1.close()


# 词性标注、过滤entity
def lexer(filename):
    '''
    1。读取文件，按 。 分词
    2。对句子词性标注
    3。过滤entity

    '''
    write_data = []
    f1 = open('test.json', 'w')
    exclude_word = ['会', '局', '院', '部', '委', '所']
    exit_entity = []
    with open(filename) as f:
        content = f.read().split('。')
    for s in content:
        entities = set(baidu_segmentation(s.strip()))
        if entities:
            for headword in entities:
                temp_dict = {
                    "head": {},
                    "relation": "",
                    "sentence": "",
                    "tail": {}
                }
                if headword[-1] not in exclude_word and len(headword) > 2:
                    headword, tailword, relation, sentence = (headword, '中兴通讯', 'NA', s)

                    if headword not in exit_entity:
                        temp_dict["head"] = {
                            "word": headword,
                            "id": str(uuid1())
                        }
                        temp_dict["tail"] = {
                            "word": tailword,
                            "id": str(uuid1())
                        }
                        temp_dict["sentence"] = ''.join(sentence)
                        temp_dict["relation"] = relation

                        write_data.append(temp_dict)
                        exit_entity.append(headword)
                        print(headword)

    f1.write(json.dumps(write_data, ensure_ascii=False, indent=2))
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
    # get_define_entity('/Users/chenhuigu/Documents/GitHub/relat_extra/origindata/Zte_notice.txt')
    # t = get_file_path_list('/Users/chenhuigu/Documents/GitHub/relat_extra/origindata')
    get_train_data()
