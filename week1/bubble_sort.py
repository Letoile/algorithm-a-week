def bubble_sort(in_data):
    data = list(in_data)
    for i, e in list(enumerate(data)):
        for j in reversed(range(i+1, len(data))):
                if data[j-1] > data[j]:
                    data[j] += data[j-1]
                    data[j-1] = data[j] - data[j-1]
                    data[j] -= data[j-1]
    return data