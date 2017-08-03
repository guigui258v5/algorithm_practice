def count_sort(l):
    max = 0
    min = 1024

    for item in l:
        if item > max:
            max = item
        elif item < min:
            min = item

    count = [0]*(max-min+1)
    for index in l:
        count[index-min] += 1

    index = 0
    for i in range(max-min+1):
        for j in range(count[i]):
            l[index] = i+min
            index += 1

if __name__ == '__main__':
    l = [6, 5, 2, 8, 9, 4, 1, 0, 3, 7]
    print(l)
    count_sort(l)
    print(l)
