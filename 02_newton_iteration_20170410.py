def newton_iteration(x):
    y = x
    while abs(y*y-x)>1e-6:
        y = (y+x/y)/2
    return y

if __name__ == '__main__':
    print(newton_iteration(10))
