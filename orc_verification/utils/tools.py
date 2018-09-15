#!/usr/share/app/anaconda3/bin/python3
# encoding: utf-8  

""" 
@version: v1.0 
@author: pu_yongjun
@license: Apache Licence
"""
import uuid
import hashlib


def gen_md5(str_con):
    """ 把输入的数据转换成MD5
    :param str_con: 输入的数据
    :return:
    """
    hl = hashlib.md5()
    hl.update(str(str_con).encode(encoding='utf-8'))
    return hl.hexdigest()


def get_arr_num(arr, num=0):
    """ 这个函数的作用是获取到数组里面的数据
    :param arr:
    :param num:
    :return:
    """
    if isinstance(arr, (tuple, list)):
        pass

    if len(arr) >= num:
        return arr[num]

    return None


def primary_md5(type_id=None, *args, **kwargs):
    """ 这个方法是生成 uuid 的md5值

    :param type_id: 类型主要是uuid的类型
    type_id 是一个枚举值，主要还是uuid本身的类型，主要如下

       1、uuid1()——基于时间戳

               由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，
               但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。

       2、uuid2()——基于分布式计算环境DCE（Python中没有这个函数）

                算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。
                实际中很少用到该方法。

      3、uuid3()——基于名字的MD5散列值

                通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，
                和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。

       4、uuid4()——基于随机数

                由伪随机数得到，有一定的重复概率，该概率可以计算出来。

       5、uuid5()——基于名字的SHA-1散列值

                算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法

    :param args: 一些uuid所需的值
    :param kwargs: 一些uuid所需的值
    :return: 返回一个uuid的md5值
    """
    uuid_dict = {
        1: uuid.uuid1,
        3: uuid.uuid3,
        4: uuid.uuid4,
        5: uuid.uuid5,
    }

    if type_id in uuid_dict.keys():
        if kwargs and (type_id in [3, 5]):
            name = kwargs.get('name')
            return gen_md5(uuid_dict.get(type_id)(uuid.NAMESPACE_DNS, name))
        else:
            return gen_md5(uuid_dict.get(type_id)())
    else:
        return gen_md5(uuid_dict.get(1)())
