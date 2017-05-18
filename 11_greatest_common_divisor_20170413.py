def greatest_common_disvisor(a, b):
    """求最大公约数,求公约数的条件是a和b都是自然数"""
    if a*b == 0:
        return max(a, b)
    while a != 0:
        a, b = b % a, a
    return b

if __name__ == '__main__':
    print(greatest_common_disvisor(90, 18))