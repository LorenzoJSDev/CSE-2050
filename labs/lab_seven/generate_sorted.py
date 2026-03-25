sorted_list = []

for i in range(1,101):
    sorted_list.append(i)

print(str(sorted_list).replace(',', '').replace('[', '').replace(']', ''))

sorted_list = []
a = 3
for i in range(1,11):
    a = a + 3
    sorted_list.append(a)

print(str(sorted_list).replace(',', '').replace('[', '').replace(']', ''))


def generate_best_case(low, high, arr):
    if low <= high:
        mid = (low + high) // 2
        arr.append(mid) # Append the median first
        # Recursively generate elements for the left and right sub-problems
        generate_best_case(low, mid - 1, arr)
        generate_best_case(mid + 1, high, arr)
    return arr

best_case_list = str(generate_best_case(1, 100, [])).replace(',', '').replace('[', '').replace(']', '')

print(best_case_list)