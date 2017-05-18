class DateValueError(ValueError):
    pass


class DateTypeError(TypeError):
    pass


class Date(object):
    def __init__(self, year, month, day):
        if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
            raise DateTypeError('输入类型错误!', year, month, day)

        if not ((month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32))
            or (month in [4, 6, 9, 11] and day in range(1, 31))
            or (month == 2 and day in range(1, 30))):  # 是闰年的情况
            raise DateValueError('%s年不存在%s月%s日' % (year, month, day))

        if not (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):  # 判断不是闰年的情况
            if month == 2 and day == 29:
                raise DateValueError('%s年不存在%s月%s日' % (year, month, day))

        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '%s-%s-%s' % (self.year, self.month, self.day)


if __name__ == '__main__':
    date1 = Date(1993, 12, 18)
    print(date1)

    # date2 = Date(1993, 2, 29)  # Error
    # print(date2)

    # date3 = Date(1993, 13, 1)  # Error
    # print(date3)

    # date4 = Date('a', 12, 1)
    # print(date4)

    date5 = Date(2000, 2, 29)  # 正常
    print(date5)

    print(type(date5))
