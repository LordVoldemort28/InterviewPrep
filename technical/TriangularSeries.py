def find_repeat(numbers_list):

    # Find the number that appears twice
    total_sum = sum(numbers_list)

    n = max(numbers_list)

    #Triangular series sum
    tri_sum = ((n*n) + n)/2

    return int(total_sum - tri_sum)


numbers_list = [4, 1, 3, 4, 2]
print(find_repeat(numbers_list))
