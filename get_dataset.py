'''
1.特例，年报或中报，词语定义中会列出所有与本公司发生关系的实体
2.循环n篇公告，file——name list
3.针对一篇公告，按句号分割，去除特殊字符，利用百度分词得到实体
    - 针对train ：entity entity relation(key) sentence
    - 针对test ：entity entity NA sentence

4.转换为训练器需要的数据格式


'''


import codecs
import json
from uuid import uuid1
from baidu_config import bd_client


# change to json
# def txt2json_data(headword, tailword, relation, sentence):






# 词性标注、过滤entity
def lexer(filename):
    '''
    1。读取文件，按 。 分词
    2。对句子词性标注
    3。过滤entity

    '''
    write_data = []
    f1 = open('test.txt','w')
    exclude_word = ['会','局','院','部','委','所']
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
                if headword[-1] not in exclude_word and len(headword)>2:
                    headword, tailword, relation, sentence = (headword,'中兴通讯','NA',s)

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
    lexer('/Users/chenhuigu/Documents/GitHub/relat_extra/origindata/Zte_notice.txt')