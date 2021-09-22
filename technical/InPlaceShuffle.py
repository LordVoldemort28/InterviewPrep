import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):

    if len(the_list) < 1:
        return the_list

    # Shuffle the input in place
    for first in range(len(the_list)):

        second = get_random(first, len(sample_list)-1)

        if first != second:
            the_list[first], the_list[second] = the_list[second], the_list[first]

    return sample_list


sample_list = [1, 2, 3, 4, 5, 6]
print(shuffle(sample_list))
