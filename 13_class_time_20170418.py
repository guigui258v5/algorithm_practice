class TimeValueError(ValueError):
    pass


class TimeTypeError(TypeError):
    pass


class Time(object):
    """时间 类"""
    def __init__(self, hou, min, sec):
        if not (isinstance(hou, int) and isinstance(min, int) and isinstance(sec, int)):
            raise TimeTypeError(hou, min, sec)

        if not (min in range(0, 61) and sec in range(0, 61)):
            raise TimeValueError(min, sec)

        self.__hou = hou
        self.__min = min
        self.__sec = sec

    def __str__(self):
        return ':'.join((str(self.__hou), str(self.__min), str(self.__sec)))

    def hours(self):
        return self.__hou

    def minutes(self):
        return self.__min

    def seconds(self):
        return self.__sec

    def __add__(self, other):
        """两个时间相加"""
        if not isinstance(other, Time):
            raise TimeTypeError('%s must be Time type' % other)
        hou, min, sec = self.__hou+other.hours(), self.__min+other.minutes(), self.__sec+other.seconds()
        if sec >= 60:
            min += sec//60
            sec = sec % 60

        if min >= 60:
            hou += min//60
            min = min % 60

        return Time(hou, min, sec)

    def __sub__(self, other):
        """两个时间相减"""
        if not isinstance(other, Time):
            raise TimeTypeError('%s must be Time type' % other)
        hou, min, sec = self.__hou-other.hours(), self.__min-other.minutes(), self.__sec-other.seconds()
        if sec >= 60:
            min += 1
            sec %= 60
        elif sec < 0:
            min -= 1
            sec += 60

        if min >= 60:
            hou += 1
            min %= 60
        elif min < 0:
            hou -= 1
            min += 60

        return Time(hou, min, sec)

    def __eq__(self, other):
        if not isinstance(other, Time):
            raise TimeTypeError('%s must be Time type' % other)
        sub_time = self.__sub__(other)
        return (sub_time.hours(), sub_time.minutes(), sub_time.seconds()) == (0, 0, 0)

    def __lt__(self, other):
        if not isinstance(other, Time):
            raise TimeTypeError('%s must be Time type' % other)
        sub_time = self.__sub__(other)
        return sub_time.hours() < 0


if __name__ == '__main__':
    time1 = Time(19, 38, 22)
    time2 = Time(20, 19, 40)
    time3 = Time(19, 38, 22)
    print(time1 - time2)
    print(time1 + time2)
    print(time1 < time2)
    print(time2 < time1)
    print(time1 == time3)
    print(time1 == time2)
