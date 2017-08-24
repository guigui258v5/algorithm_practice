import random


# 原有生成１－５随机数的函数
def random_5():
    return random.randint(1, 5)


# 要获得的生成１～７随机数的函数
def random_7():
    while True:  # 避免没有返回值
        n = (random_5()-1)*5 + random_5()  # 生成１～２５的随机数
        if n <= 21:
            return n%7 + 1


if __name__ == '__main__':
    print(random_7())
