import random
import math


class RandomIJToRandomAB(object):
    """将原来i-j之间的随机数生成函数，转化为a-b之间的随机数生成函数"""
    def __init__(self, i, j):
        self.i = i
        self.j = j
        ij_dif = j-i

        if ij_dif <= 0:
            raise ValueError

        self.ij_dif = ij_dif

    def random_ij(self):
        return random.randint(0, self.ij_dif)

    def random_ab(self, a, b):
        ab_dif = b-a
        digit = int(math.ceil(math.log(ab_dif+1, self.ij_dif+1)))  # 获取差值(ab_dif)转换为ij_dif+1进制后的最大位数

        while True:  # 防止return None
            # 生成最大位数为digit的ij_dif+1进制随机数，而后转化为10进制
            random_res = 0
            for item in range(digit):
                random_res += self.random_ij() * pow(self.ij_dif+1, item)

            # 只取在区间范围内的随机数
            if random_res <= ab_dif:
                return random_res+a


if __name__ == '__main__':
    print('0~1随机生成函数转化为２~11随机生成函数')
    random_1 = RandomIJToRandomAB(0, 1)
    print(random_1.random_ab(2, 11))
    print('-'*50)

    print('1~5随机生成函数转化为１~7随机生成函数')
    random_1_5 = RandomIJToRandomAB(1, 5)
    print(random_1_5.random_ab(1, 7))
    print('-'*50)

    print('1~7随机生成函数转化为１~5随机生成函数')
    random_1_7 = RandomIJToRandomAB(1, 7)
    print(random_1_7.random_ab(1, 5))
    print('-'*50)
