from datetime import datetime

#Dynammic programming(Memoization)
def getNthFib2(n, mem={1: 0, 2: 1}):
    if n <= len(mem):
        return mem[n]
    else:
        mem[n] = getNthFib2(n-1, mem) + getNthFib2(n-2, mem)
        return mem[n]

#Tail Recursion technique
#Much memory efficient and faster than memoization
#Same technique can be used for calculating factorial
def getNthFib(n):

    array = [0, 1]

    if n <= 2:
        return array[n-1]

    counter = 3

    while counter <= n:

        next = array[0] + array[1]
        array[0] = array[1]
        array[1] = next

        counter += 1

    return array[1]


start = datetime.now()
getNthFib(999)
end = datetime.now()
print((end-start))


start = datetime.now()
getNthFib2(999)
end = datetime.now()
print(float(end-start))

