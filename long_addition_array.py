first_num = [8, 2, 4, 5, 5, 5]
second_num = [4, 5, 6, 5, 5, 5]

def add_big(first_num, second_num):
    # resultant list
    result = []
    # initialise variables
    first_num_len = len(first_num)
    second_num_len = len(second_num)
    """
    check whether the length of either list is longer than the other.
    add 0 to the start of the list if its longer. number of 0 depends on
    the difference in length
    """
    if first_num_len > second_num_len:
        for j in range(first_num_len - second_num_len):
            second_num.insert(0, 0)
    elif first_num_len < second_num_len:
        for j in range(second_num_len - first_num_len):
            first_num.insert(0, 0)

    # addition function
    for i in range(len(first_num)):
        int1 = first_num[i]
        int2 = second_num[i]
        int_result = int1 + int2
        result.append(int_result)

    # carry over function
    for j in range(len(result)-1, 1, -1):
        if result[j] >= 10:
            result[j] -= 10
            result[j-1] += 1
    result = [int(x) for z in result for x in str(z)]
    return result

print(add_big(first_num, second_num))
