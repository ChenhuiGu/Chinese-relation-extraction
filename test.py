# import tensorflow as tf
#
# a = tf.constant([1.0,2.0],name='a',dtype=tf.float16)
# b = tf.constant([4,5],name='b',dtype=tf.float16)
#
# result = tf.add(a,b)
#
# print(result)
#
# print(tf.Session().run(result))

# key_words = {
#         '持有股票': ['股票', '股东', ],
#         '合作': ['联合', '合作', '携手'],
#         '关联': ['关联'],
#         '担保': ['担保'],
#         '供应商': ['供应', '供货'],
#         '客户': ['客户'],
#         '投资子公司': ['投资子公司'],
#         '法律纠纷': ['法律纠纷'],
#         '竞争对手': ['竞争对手'],
#         '子公司': ['子公司']
#     }
#
# print(list(key_words.keys())[0])
# print(list(key_words.values())[0])


# s = '施混合所有制改革从而提升公司多媒体业务的竞争力线上彩电品牌引入了广东南方爱视娱乐科技有限公司作为股东是一家专业提供家庭互联网电视娱乐服务的互联网公司拥有全牌照的联合运营权丰'
#
# from get_dataset import baidu_segmentation
#
# entitys = baidu_segmentation(s)
#
# for entity in entitys:
#     print(s.index(entity))
#
# print(entitys)



# 云脑科技面试题（同学的）2018-05-24 下午
# 解题思路：二分查找，寻找最佳位置，如果存在返回索引mid，如果不存在返回应该插入的索引mid（保持有序）
# 如果 0 < mid < n:  # 说明找到了或者没找到，但是应该插入数列的内部，从最佳位置向两边查找，找出所有的最近数字
# 如果 mid == 0:  # 小于最左边的数字，只向右查找，找出所有的最近数字
# 如果 mid == n:  # 大于最右边的数字，只向左查找，找出所有的最近数字
# 如果 数组为空 返回 -1


# def searchInsert(nums, target):  # 二分查找，如果找到，返回下标索引，没有则返回应该插入的位置（保持有序）
#     start = 0
#     end = len(nums) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return end + 1
#
#
# def rIndex(nums, target):
#
#     n = len(nums)
#     if n == 0: return -1
#     mid = searchInsert(nums, target)
#     rlist = []  # 保持索引
#     i, j = -1, n
#     left, rigth = 0, 0  # 左右扩展的标志
#     mxg = float('-inf')
#     if 0 < mid < n:  # 如果找到了
#         i, j = mid-1, mid
#         mxg = min(abs(nums[i] - target), abs(nums[j] - target))
#         left, rigth = 1, 1
#     elif mid == 0:  # 小于最左边的数字
#         j = mid
#         mxg = abs(nums[j] - target)
#         left, rigth = 0, 1
#     elif mid == n:  # 大于最右边的数字
#         i = mid-1
#         mxg = abs(nums[i] - target)
#         left, rigth = 1, 0
#
#     while left == 1 or rigth == 1:  # 两边查找
#         if i == -1: left = 0
#         if j == n: rigth = 0
#         if left == 1 and i >= 0:
#             le = abs(nums[i] - target)
#             if le == mxg:
#                 rlist = [i] + rlist
#                 i -= 1
#             else:
#                 left = 0
#         if rigth == 1 and j < len(nums):
#             ri = abs(nums[j] - target)
#             if mxg == ri:
#                 rlist = rlist + [j]
#                 j += 1
#             else:
#                 rigth = 0
#     return rlist


# def change_encode():
#     file = '/Users/chenhuigu/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/relat_extra/train_data.csv'
#     f = open(file)
#     f1 = open('test.csv', 'w')
#     content = f.read()
#
#     content.encode('gbk').decode('gbk')
#     f1.write(content)
#     f.close()
#     f1.close()

if __name__ == '__main__':
    read_csv()
