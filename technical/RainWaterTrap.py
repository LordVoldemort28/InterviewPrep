def get_max(arr):
    return max(arr) if len(arr) else 0


def trap_rainBruteForce(heights):

    left_max, right_max = float("-inf"), float("-inf")
    total_water = 0

    for idx, height in enumerate(heights):

        left_max = get_max(heights[:idx])
        right_max = get_max(heights[idx:])

        water = min(left_max, right_max) - height

        if water > 0:
            total_water += water

    return total_water

def trap_rain(height):
    waterLevel = []
    left = 0
    for h in height:
        left = max(left, h)
        waterLevel += [left]  # over-fill it to left max height
    right = 0
    for i, h in reversed(list(enumerate(height))):
        right = max(right, h)
        waterLevel[i] = min(waterLevel[i], right) - h  # drain to the right height
    return sum(waterLevel)


print(trap_rain([4, 2, 0, 3, 2, 5]))
print(trap_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
