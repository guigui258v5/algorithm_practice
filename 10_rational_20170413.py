class Rational(object):
    @staticmethod
    def __gcd(a, b):
        """求最大公约数,求公约数的条件是a和b都是自然数"""
        if a * b == 0:
            return max(a, b)
        while a != 0:
            a, b = b % a, a
        return b

    def __init__(self, num, den=1):
        if (not (isinstance(num, int) and isinstance(den, int)))\
                and (not (den == 1 and isinstance(num, float))):
            raise TypeError

        if isinstance(num, int):  # 从分数构造有理数
            sign = 1
            if den == 0:
                raise ZeroDivisionError
            if den < 0:
                den, sign = -den, -sign
            if num == 0:
                sign = 0
            if num < 0:
                num, sign = -num, -sign

            gcd = Rational.__gcd(num, den)
            self.__num = sign*num//gcd  # 为返回int而不是float,需要用floor除法
            self.__den = den//gcd  # 有理数应为不可变类型,所以定义为私有属性
            self.__sign = sign  # 保存符号,在比较大小或者判断正负的时候可以用到

        elif isinstance(num, float):  # 从浮点数构造有理数
            self.__sign = 1
            if num < 0:
                self__sign, num = -self.__sign, -num
            self.__num, self.__den = num.as_integer_ratio()
            self.__num *= self.__sign

    def __str__(self):
        return str(self.__num) + '/' + str(self.__den)

    def num(self):
        return self.__num

    def den(self):
        return self.__den

    def sign(self):
        return self.__sign

    def __add__(self, other):
        """加法"""
        if not isinstance(other, Rational):  # 检查对方是否2为有理数对象
            raise TypeError
        den = self.__den*other.den()
        num = self.__num*other.den() + other.num()*self.__den
        return Rational(num, den)

    def __sub__(self, other):
        """减法"""
        if not isinstance(other, Rational):
            raise TypeError
        num = self.__num*other.den() - other.num()*self.__den
        den = self.__den*other.den()
        return Rational(num, den)

    def __mul__(self, other):
        """乘法"""
        if not isinstance(other, Rational):
            raise TypeError
        num = self.__num*other.num()
        den = self.__den*other.den()
        return Rational(num, den)

    def __floordiv__(self, other):
        """floor除法"""
        if not isinstance(other, Rational):
            raise TypeError
        if other.num == 0:
            raise ZeroDivisionError
        num = self.__num*other.den()
        den = self.__den*other.num()
        return Rational(num, den)

    def __gt__(self, other):
        return self.__sub__(other).sign() == 1

    def __eq__(self, other):
        return self.__sub__(other).sign() == 0

    def __lt__(self, other):
        return self.__sub__(other).sign() == -1

    def to_int(self):
        return int(self.__num/self.__den)

    def to_float(self):
        return self.__num/self.__den

if __name__ == '__main__':
    a = Rational(6, 9)
    b = Rational(15, -7)
    print(a)
    print(b)

    # 加减乘除
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)

    # 比较大小
    print(a>b)
    print(a==b)
    print(a<b)

    # 输出类型
    print(type(a))
    print(type(b))

    print(b.to_int())
    print(b.to_float())

    c = Rational(-2.5)  # 从浮点数构造有理数
    print(c)
