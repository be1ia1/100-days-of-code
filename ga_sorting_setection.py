"""reproduce sorting selection algoritm"""
data = [33, 23, 29, 4, 88, 18, 25]

def get_smaller(array):
    smaller = array[0]
    for num in array[1:]:
        if num < smaller:
            smaller = num
    return smaller

def sorting_selection():
    answer = []
    for _ in range(0, len(data)):
        num = get_smaller(data)
        answer.append(num)
        data.remove(num)
    return answer

print(sorting_selection())

