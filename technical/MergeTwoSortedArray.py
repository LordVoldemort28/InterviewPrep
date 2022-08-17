def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    if not len(my_list):
        return alices_list

    if not len(alices_list):
        return my_list

    i, j, k = 0, 0, 0

    merge_list = [0] * (len(my_list)+len(alices_list))

    while i < len(my_list) and j < len(alices_list):
        if my_list[i] < alices_list[j]:
            merge_list[k] = my_list[i]
            i += 1
        else:
            merge_list[k] = alices_list[j]
            j += 1
        k += 1

    while i < len(my_list):
        merge_list[k] = my_list[i]
        i += 1
        k += 1

    while j < len(alices_list):
        merge_list[k] = alices_list[j]
        j += 1
        k += 1

    return merge_list


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12]

print(merge_lists(my_list, alices_list))

# actual = merge_lists([], [])
#     expected = []

# def test_first_list_is_empty(self):
#     actual = merge_lists([], [1, 2, 3])
#     expected = [1, 2, 3]

# def test_second_list_is_empty(self):
#     actual = merge_lists([5, 6, 7], [])
#     expected = [5, 6, 7]

# def test_both_lists_have_some_numbers(self):
#     actual = merge_lists([2, 4, 6], [1, 3, 7])
#     expected = [1, 2, 3, 4, 6, 7]

# def test_lists_are_different_lengths(self):
#     actual = merge_lists([2, 4, 6, 8], [1, 7])
#     expected = [1, 2, 4, 6, 7, 8]
