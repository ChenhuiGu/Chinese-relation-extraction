'''
1.entity entity(keyword) relation --.senstences
2.entity 与 id dict
3.get senstence
4.json文件
'''
import json
import os
import re
import traceback
from uuid import uuid1
# import pandas as pd
import Config

# def get_entity_id_dict():
#     dict = {}
#     file_name = '/Users/chenhuigu/Documents/GitHub/relat_extra/origindata/company_list.csv'
#     df = pd.read_csv(file_name)
#     for i in range(19):
#         dict[df['公司'][i]] = df['id'][i]
#     return dict

company_id_dict = {'中国神华': 1457634, '万华化学': 1684580, '恒力股份': 1051191, '洛阳钼业': 566883,
                   '中国重工': 1693746, '宁德时代': 27454, '国电南瑞': 1056221, '三一重工': 196288,
                   '中国中车': 1059672, '中国国航': 205716, '上海机场': 1679245, '分众传媒': 1269467,
                   '中兴通讯': 567337, '中国联通': 4717, '上汽集团': 743468, '三六零': 16407, '美的集团': 567434,
                   '海螺水泥': 1891489, '立讯精密': 974440}

def id2filepath(id):
    '''
    :param id:
    :return: file path
    '''
    base_dir = '/data01/guchh/df-copy'
    id = int(id)
    if 700000 <= id < 1300000:
        dir = str(id % 60)
        dirpath = os.path.join(base_dir, dir)
    elif id > 1891489 or id < 700000:
        dir = str(id % 200)
        dirpath = os.path.join(base_dir, dir)
    else:
        dir = str(id % 70)
        dirpath = os.path.join(base_dir, dir)
    filepath = dirpath + '/%d.txt' % id
    return filepath


def read_notice():
    '''
    获取文本信息，根据关键词获取senstence
    :param file_path:
    :return:
    '''
    content_cache = {}
    write_data = []
    file_path = Config.ORIGIN_DATA + 'traindata-01.csv'
    f1 = open(Config.CN_DATA + 'traindata.json','a')
    with open(file_path) as f:
        # 获取全部文本
        items = f.readlines()
    for item in items:
        temp_dict = {
            "head": {},
            "relation": "",
            "sentence": "",
            "tail": {}
        }
        headword,tailword, relation = tuple(item.strip().split(','))
        if headword not in content_cache.keys():
            file2_path = id2filepath(company_id_dict[headword])
            try:
                with open(file2_path) as f:
                    content = f.read()
                list = re.findall(r'.*%s.*' % tailword, content)
                sentence = ','.join(list[1:])
                content_cache[headword] = content
            except Exception:
                print(traceback.format_exc())
        else:
            content = content_cache[headword]
            list = re.findall(r'.*%s.*' % tailword, content)
            sentence = ','.join(list[1:])

        temp_dict["head"] = {
            "word": headword,
            "id": str(uuid1())
        }
        temp_dict["tail"] = {
            "word": tailword,
            "id": str(uuid1())
        }

        temp_dict["sentence"] = sentence
        temp_dict["relation"] = relation


        write_data.append(temp_dict)
        print(tailword)
    f1.write(json.dumps(write_data, ensure_ascii=False, indent=2))
    f.close()


if __name__ == '__main__':
    read_notice()
