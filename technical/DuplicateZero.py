class DuplicateZero:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):

            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop(len(arr)-1)
                i += 2
            else:
                i += 1

        return arr


example1 = [1, 0, 2, 3, 0, 4, 5, 0]
sol = DuplicateZero()
sol.duplicateZeros(example1)
