
def quicksort_last_element(array):
    def quicksort_and_count(array, start, end):
        if start < end:
            pivot_index, comparisons = partition(array, start, end)
            total_comparisons = (comparisons +
                                 quicksort_and_count(array, start, pivot_index - 1) +
                                 quicksort_and_count(array, pivot_index + 1, end))
            return total_comparisons
        else:
            return 0

    def partition(array, start, end):
        array[start], array[end] = array[end], array[start]
        pivot = array[start]
        i = start + 1
        for j in range(start + 1, end + 1):
            if array[j] < pivot:
                array[j], array[i] = array[i], array[j]
                i += 1
        array[start], array[i - 1] = array[i - 1], array[start]
        return i - 1, end - start

    return quicksort_and_count(array, 0, len(array) - 1)

file_path = '/mnt/data/integer_Array.txt'
with open(file_path, 'r') as file:
    array = [int(line.strip()) for line in file.readlines()]

total_comparisons = quicksort_last_element(array)
total_comparisons
