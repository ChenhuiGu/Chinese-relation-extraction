import codecs
import json
from uuid import uuid1


def txt2json_dict(readfile, writefile):
    f = codecs.open(readfile, 'r', 'utf-8')
    f2 = codecs.open(writefile, 'w', 'utf-8')

    write_dict = {}
    for line in f:
        key, value = line.strip().split()
        write_dict[key] = value

    f2.write(json.dumps(write_dict, ensure_ascii=False, indent=2))

    f.close()
    f2.close()


def txt2json_vec(readfile, writefile, fromline):
    f = codecs.open(readfile, 'r', 'utf-8')
    f2 = codecs.open(writefile, 'w', 'utf-8')

    write_data = []
    lines = f.readlines()
    for line in lines[fromline:]:
        temp_dict = {}
        splitdata = line.strip().split()

        word, vec = splitdata[0], splitdata[1:]

        temp_dict["word"] = word
        temp_dict["vec"] = vec

        write_data.append(temp_dict)

    f2.write(json.dumps(write_data, ensure_ascii=False, indent=2))


    f.close()
    f2.close()



def txt2json_data(readfile, writefile):
    f = codecs.open(readfile, 'r', 'utf-8')
    f2 = codecs.open(writefile, 'w', 'utf-8')

    write_data = []
    for line in f:
        temp_dict = {
            "head": {},
            "relation": "",
            "sentence": "",
            "tail": {}
        }
        splitdata = line.strip().split()

        headword, tailword, relation, sentence = splitdata[0], splitdata[1], splitdata[2], splitdata[3:]

        if len(write_data) > 0:
            # 验证是否存在重复字段
            for item in write_data:
                if item["head"] and item["head"]["word"] == headword:
                    temp_dict["head"] = item["head"]
                elif item["tail"] and item["tail"]["word"] == headword:
                    temp_dict["head"] = item["tail"]
                else:
                    temp_dict["head"] = {
                        "word": headword,
                        "id": str(uuid1())
                    }

                if item["head"] and item["head"]["word"] == tailword:
                    temp_dict["tail"] = item["head"]
                elif item["tail"] and item["tail"]["word"] == tailword:
                    temp_dict["tail"] = item["tail"]
                else:
                    temp_dict["tail"] = {
                        "word": tailword,
                        "id": str(uuid1())
                    }
        else:
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
        
    f2.write(json.dumps(write_data, ensure_ascii= False, indent=2))
    f.close()
    f2.close()


def remove_nan():
    # f = open('/Users/chenhuigu/Documents/GitHub/relat_extra/data/cndata/validata.json','w')
    # datas = json.loads(open('/Users/chenhuigu/Documents/GitHub/relat_extra/data/cndata_cp/validata.json').read())
    datas = json.loads(open('/Users/chenhuigu/Documents/GitHub/relat_extra/data/cndata/testdata.json').read())
    for i in range(1):
        for data in datas:
            if data['sentence'] == '':
                print(data)
                # datas.remove(data)
    # f.write(json.dumps(datas, ensure_ascii=False, indent=2))
    # f.close
import random
def add_headword():
    '''将2个实体都加入到句子中,位置随机(插入主体之中)/句子末尾'''

    f = open('/Users/chenhuigu/Documents/GitHub/relat_extra/data/cndata/validata.json','w')
    datas = json.loads(open('/Users/chenhuigu/Documents/GitHub/relat_extra/data/cndata_cp3/validata.json').read())
    for data in datas:
        index = random.randint(0,len(data['sentence'])-1)
        data['sentence'].insert(data['head']['word'])

    f.write(json.dumps(datas, ensure_ascii=False, indent=2))
    f.close
if __name__ == '__main__':

    # txt2json_dict('./origindata/relation2id.txt', './data/cndata/rel2id1.json')
    add_headword()
