'''
通过公告获取公司供应链
1.获取公告内的公司实体
2.解析实体关系

问题：
1.去除本公司的常用名
'''

import config
from utils import get_blocks
from baidu_config import bd_client
import traceback

def _get_company_entity():
    '''
    获取公司实体
    :return: entity list
    '''
    # 读取公告
    # 调用百度接口(限制5000字),返回分词、实体、概念
    items = read_notice()
    for item in items:
        try:
            vocabulary, entities = baidu_segmentation(item)
            list2file(vocabulary,'word.txt')
            list2file(entities,'company.txt')
        except Exception:
            print(traceback.format_exc())


def read_notice(file_path=''):
    '''
    获取文本信息，对文本进行预处理
    :param file_path:
    :return:
    '''
    file_path = config.base_dir + '/data/Zte_notice.txt'
    with open(file_path) as f:
        # 获取全部文本
        item = f.readlines()[0]
    iterator = get_blocks(item, 4000)
    return iterator


def list2file(list, name):
    '''将列表写入文件中'''
    words = ','.join(list)
    file_path = config.base_dir + '/data/lexer_result/' + name
    with open(file_path, 'a') as f:
        f.write(words)




if __name__ == '__main__':
    _get_company_entity()
