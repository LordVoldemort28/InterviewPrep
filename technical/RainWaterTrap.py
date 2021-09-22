def get_max(arr):
    return max(arr) if len(arr) else 0


def trap_rain(heights):

    left_max, right_max = float("-inf"), float("-inf")
    total_water = 0

    for idx, height in enumerate(heights):

        left_max = get_max(heights[:idx])
        right_max = get_max(heights[idx:])

        water = min(left_max, right_max) - height

        if water > 0:
            total_water += water

    return total_water


print(trap_rain([4, 2, 0, 3, 2, 5]))
print(trap_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
