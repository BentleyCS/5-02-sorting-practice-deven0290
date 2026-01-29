def bubbleSort(items: list):
    swaps = 0
    comparisons = 0
    n = len(items)

    while True:
        didSwap = False

        for i in range(n - 1):
            comparisons += 1
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swaps += 1
                didSwap = True

        if not didSwap:
            break

    return items, swaps, comparisons


def insertionSort(items: list):
    swaps = 0
    comparisons = 0

    for i in range(1, len(items)):
        key = items[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if items[j] > key:
                items[j + 1] = items[j]  
                swaps += 1               
                j -= 1
            else:
                break

        items[j + 1] = key

    return items, swaps, comparisons


def selectionSort(items: list):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if items[j] < items[min_index]:
                min_index = j

        items[i], items[min_index] = items[min_index], items[i]
        swaps += 1

    return items, swaps, comparisons
